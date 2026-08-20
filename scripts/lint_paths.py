#!/usr/bin/env python3
"""Fail the build when deployment-path content drifts out of its path block.

The workshop supports two deployment paths. A reader picks one on the gate page
and every later page must follow that choice, which only works if *every*
path-specific instruction lives inside a ``pathtabs`` block (or on a page whose
front matter declares a single ``deploymentPath``). A ``kubectl`` command sitting
in unbranched prose is invisible to that mechanism: the Docker reader sees it and
has no way to know it does not apply to them.

This linter is the guardrail for that invariant. It checks:

1. path-like titles in a plain ``tabs`` group -- a hand-rolled path switch that
   does not synchronise with the reader's choice
2. hand-written ``groupid="deploy-path"`` -- bypasses the pathtabs shortcode and
   its missing-path check
3. path-specific tokens outside a path block -- with an explicit allowlist below.
   Fenced code is checked too: a bare ``kubectl`` fence outside a path block is the
   most likely place for this leak to appear, not the least
4. ``cd "~`` anywhere -- bash does not expand ``~`` inside double quotes, so the
   command always fails
5. block markup that either tool would silently mis-parse: a block written with the
   other delimiter form, an unknown ``path=`` key, a path block nested in another, a
   marker sharing a line with anything else, and any block still open at end of file
6. stale generated handouts (delegates to ``gen_handouts.py --check``)

Usage
-----
    python3 scripts/lint_paths.py            # lint, exit 1 on any violation
    python3 scripts/lint_paths.py --list     # print the config and exit

Reusing this in another workshop repo: take ``gen_handouts.py`` with it -- this file
imports the path vocabulary and the marker grammar from it -- then keep the CONFIG
block's structure and empty out ``PATH_TITLE_RE``, ``PATH_TOKENS`` and ``ALLOWLIST``.
Checks 1 and 3 then no-op and the repo still gets checks 2, 4 and 5.

This is that reused copy, in ``UserRepo``: ``PATH_TITLE_RE``, ``PATH_TOKENS`` and
``ALLOWLIST`` below are emptied per the instructions above, since ai-101's docker/k8s
vocabulary would otherwise false-positive on this repo's own prose about the
deployment-path feature (which names Docker and Kubernetes constantly as its worked
example). ``gen_handouts.py``'s ``deploymentPaths`` no-op handles the separate case of
a repo, like this one by default, that has not opted into the feature at all.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# The marker grammar and the path vocabulary are the handout generator's, imported
# rather than restated. Two copies of "what a marker looks like" is this linter's own
# failure mode one level up: when the two scripts disagree, the linter passes a page the
# generator cannot parse, or reports a block the generator ignores. A plain sibling
# import works because this script is always run as a script, so ``sys.path[0]`` is
# ``scripts/`` -- the two files travel together as a pair.
#
# This also makes the linter depend on scripts/repoConfig.json, which is where the
# generator reads the paths from. Deliberate: a linter enforcing a vocabulary the site
# is not built with would be worse than one that refuses to start.
from gen_handouts import (
    BLOCK_DELIMS,
    BLOCK_MARKER_RE,
    FENCE_RE,
    FRONT_MATTER_DELIM,
    PATHS,
    marker_form,
)

# ==========================================================================
# CONFIG -- the path vocabulary. Everything repo-specific lives in this block.
# ==========================================================================

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT = REPO_ROOT / "content"

# Generated single-path pages. Path tokens outside pathtabs are the whole point
# there, so the token checks would be nothing but false positives. Their
# freshness is checked separately (check 6).
GENERATED_DIRS = [CONTENT / "09Reference" / "handouts"]

# Front-matter key that marks a whole page as belonging to one path.
PAGE_PATH_KEY = "deploymentPath"

# Keys accepted by the pathtab/pathonly shortcodes, which now live in CentralRepo and
# read `deploymentPaths` from scripts/repoConfig.json. Derived, not restated: PATHS is
# itself built from that file, so this linter enforces the same vocabulary Hugo builds
# with. Adding a path is a one-file edit.
PATH_KEYS = [p["key"] for p in PATHS]

# A tab title matching this is a path switch. Catching it in a plain `tabs` group
# is the point: such a group has its own random groupid, so clicking it does not
# follow the reader's choice on any other page.
#
# Empty in this copy -- ai-101's vocabulary (docker/kubernetes/helm) is that
# workshop's content, not this repo's. See the reuse note in the module docstring.
# A pattern that can never match, rather than an empty alternation (which errors).
PATH_TITLE_RE = re.compile(r"(?!)")

# Tokens that only make sense on one path. Each is (label, regex).
#
# Commands are the obvious half and were the whole list to begin with. Both leaks
# that actually shipped were the other half -- prose naming one path's runtime as
# *the* way the lab is wired: "the agent container reaches the MCP server container
# at ... using the Docker service hostname" (content/04MCP/_index.md) and "Docker
# Engine + Compose v2" (content/_index.md). To a Kubernetes reader, who has no Docker
# daemon at all, that reads as authoritative rather than as one of two options, which
# is the same harm as an unbranched `docker compose` command.
# Tokens that only make sense on one path, keyed (label, regex) -- ai-101's list.
# Empty in this copy: this repo has no lab content to leak a runtime detail from, and
# the tokens below (docker/kubectl/helm/...) are exactly the words this repo's own
# documentation about the deployment-path feature uses as its worked example. See the
# reuse note in the module docstring. A repo that copies this file and does write
# path-specific lab content should repopulate this list the way ai-101 did.
PATH_TOKENS: list[tuple[str, re.Pattern]] = []

# Lines allowed to carry a path token outside a path block. Each entry needs a
# reason -- if you cannot write one, the line probably belongs in a pathtabs block.
#
# ``file`` is relative to content/ (or None for any file); ``match`` must appear
# in the line.
#
# Empty in this copy -- these entries were ai-101's gate page (01Intro/_index.md),
# which does not exist here. See the reuse note in the module docstring.
ALLOWLIST: list[dict] = []

# ==========================================================================
# Implementation
# ==========================================================================

# Backticked prose is not markup. A sentence mentioning `{{< pathtabs >}}` inline used
# to flip the tracker on and suppress every path-token check to the end of the file,
# and skipping fenced code never helped -- inline code is not a fence.
INLINE_CODE_RE = re.compile(r"`+[^`]*`+")

# Blocks whose body is scoped to one path, so path tokens inside them are already
# branched. They may not nest: see the nested-path-block violation below.
PATH_BLOCKS = ("pathtabs", "pathonly")

# ``pathonly`` takes exactly one attribute. Anything else is either a typo or an
# attempt to grow the signature, which the handout generator's anchored marker
# regexes would stop matching -- silently, producing a handout with the shortcode
# still in it.
PATHONLY_ARGS_RE = re.compile(r'^\s*path="([^"]+)"\s*$')

TAB_TITLE_RE = re.compile(r"\{\{%\s*tab\s+[^%]*title=\"([^\"]+)\"")
GROUPID_RE = re.compile(r"groupid\s*=\s*\"deploy-path\"")
BAD_TILDE_RE = re.compile(r'cd\s+"~')


class Violation:
    def __init__(self, path: Path, line_no: int, check: str, detail: str, line: str):
        self.path = path
        self.line_no = line_no
        self.check = check
        self.detail = detail
        self.line = line.strip()

    def __str__(self) -> str:
        rel = self.path.relative_to(REPO_ROOT)
        return f"{rel}:{self.line_no}: [{self.check}] {self.detail}\n    {self.line}"


def front_matter_value(lines: list[str], key: str) -> str | None:
    if not lines or lines[0].strip() != FRONT_MATTER_DELIM:
        return None
    for raw in lines[1:]:
        if raw.strip() == FRONT_MATTER_DELIM:
            return None
        m = re.match(rf"^{key}\s*:\s*(.*)$", raw.strip())
        if m:
            return m.group(1).strip().strip('"').strip("'")
    return None


def allowed(rel_md: Path, line: str) -> bool:
    for entry in ALLOWLIST:
        if entry["file"] is not None and Path(entry["file"]) != rel_md:
            continue
        if entry["match"] in line:
            return True
    return False


def content_pages() -> list[Path]:
    pages = []
    for md in sorted(CONTENT.rglob("*.md")):
        if md.name not in ("index.md", "_index.md"):
            continue
        if any(gen in md.parents for gen in GENERATED_DIRS):
            continue
        pages.append(md)
    return pages


def lint_page(md: Path) -> list[Violation]:
    lines = md.read_text(encoding="utf-8").splitlines()
    rel_md = md.relative_to(CONTENT)
    page_path = front_matter_value(lines, PAGE_PATH_KEY)
    violations: list[Violation] = []

    # A page declaring a single deploymentPath is itself a path block, so tokens
    # anywhere on it are already scoped. Its marker must still be a real path.
    if page_path and page_path not in PATH_KEYS:
        violations.append(
            Violation(md, 1, "page-marker", f"unknown {PAGE_PATH_KEY}: {page_path!r}", page_path)
        )
    page_is_path_scoped = page_path in PATH_KEYS

    fence: str | None = None
    # Depths, not booleans. As booleans the first close ended a nested group, and the
    # outer block's remaining lines were then treated as unbranched prose.
    depth = {"pathtabs": 0, "pathonly": 0, "tabs": 0}

    for i, line in enumerate(lines, start=1):
        m = FENCE_RE.match(line)
        if fence is not None:
            if m and line.strip().startswith(fence):
                fence = None
            in_fence = True
        elif m:
            fence = m.group(1)[0] * 3
            in_fence = True
        else:
            in_fence = False

        if BAD_TILDE_RE.search(line):
            violations.append(
                Violation(
                    md,
                    i,
                    "tilde-in-quotes",
                    'bash does not expand ~ inside double quotes; use cd ~/... or "$AI101_HOME/..."',
                    line,
                )
            )

        # Every check that reads *markup* skips fenced code, and each for its own
        # reason: a fenced ``{{< pathtabs >}}`` documents the shortcode rather than
        # using it, and flipping a tracker on it would suppress the token check for the
        # rest of the page; a fenced groupid="deploy-path" is likewise an example of
        # what not to write. The token check below deliberately does *not* skip fences.
        opened_here: set[str] = set()
        if not in_fence:
            if GROUPID_RE.search(line):
                violations.append(
                    Violation(
                        md,
                        i,
                        "handwritten-groupid",
                        'use the pathtabs shortcode instead of groupid="deploy-path"',
                        line,
                    )
                )

            markup = INLINE_CODE_RE.sub(" ", line)
            markers = list(BLOCK_MARKER_RE.finditer(markup))
            for marker in markers:
                name = marker.group("name")
                if marker.group("delim") != BLOCK_DELIMS[name]:
                    violations.append(
                        Violation(
                            md,
                            i,
                            "wrong-delimiter",
                            f"write {name} as {marker_form(name)} -- the delimiter is part "
                            "of the shortcode's contract, and the wrong one fails silently: "
                            "the block renders, but ungated, and any heading inside it drops "
                            "out of the page's fragment set so in-page links to it go dead",
                            line,
                        )
                    )
                if marker.group("close") is not None:
                    depth[name] = max(0, depth[name] - 1)
                    continue
                if name in PATH_BLOCKS and (depth["pathtabs"] or depth["pathonly"]):
                    violations.append(
                        Violation(
                            md,
                            i,
                            "nested-path-block",
                            f"a {name} block inside another path block is either redundant (same "
                            "path) or dead content (the other path); move it out, or let the "
                            "enclosing block's body carry the text",
                            line,
                        )
                    )
                if name == "pathonly":
                    args = PATHONLY_ARGS_RE.match(marker.group("args"))
                    if not args:
                        violations.append(
                            Violation(
                                md,
                                i,
                                "pathonly-args",
                                'pathonly takes exactly one attribute: path="KEY", where KEY is '
                                f"one of {', '.join(PATH_KEYS)}",
                                line,
                            )
                        )
                    elif PATH_KEYS and args.group(1) not in PATH_KEYS:
                        # No site-level PATH_KEYS means no site vocabulary to check
                        # against -- a page can declare its own deploymentPaths in
                        # front matter instead (see content/02Hugo/6_deployment_paths),
                        # and this linter has no way to see that page-scoped list, so
                        # it stays silent rather than rejecting a key it cannot know.
                        violations.append(
                            Violation(
                                md,
                                i,
                                "unknown-path",
                                f"unknown path {args.group(1)!r}; use one of "
                                f"{', '.join(PATH_KEYS)}",
                                line,
                            )
                        )
                depth[name] += 1
                opened_here.add(name)

            if markers and (len(markers) > 1 or BLOCK_MARKER_RE.sub("", markup).strip()):
                violations.append(
                    Violation(
                        md,
                        i,
                        "marker-not-alone",
                        "put each block marker alone on its own line -- gen_handouts.py matches "
                        "them anchored to the whole line, so a shared line is never flattened and "
                        "ships into the handout as a raw shortcode",
                        line,
                    )
                )

            # ``opened_here`` covers a group opened and closed on one line, whose depth
            # is already back to zero by the time the title is inspected.
            if depth["tabs"] or "tabs" in opened_here:
                title = TAB_TITLE_RE.search(line)
                if title and PATH_TITLE_RE.search(title.group(1)):
                    violations.append(
                        Violation(
                            md,
                            i,
                            "path-tab-outside-pathtabs",
                            f"tab title {title.group(1)!r} looks like a deployment path; "
                            "use pathtabs so it follows the reader's choice",
                            line,
                        )
                    )

        in_path_block = bool(
            depth["pathtabs"] or depth["pathonly"] or opened_here.intersection(PATH_BLOCKS)
        )
        if in_path_block or page_is_path_scoped:
            continue
        if allowed(rel_md, line):
            continue
        for label, token in PATH_TOKENS:
            if token.search(line):
                violations.append(
                    Violation(
                        md,
                        i,
                        "token-outside-path-block",
                        f"{label!r} is path-specific; wrap it in pathtabs, set "
                        f"{PAGE_PATH_KEY} on the page, or add an allowlist entry with a reason",
                        line,
                    )
                )
                break

    # An unbalanced block is what makes a tracker leak, and a leaked tracker is silent
    # -- it suppresses checks rather than reporting anything. Hugo also rejects an
    # unclosed shortcode, but only once the block is genuinely unclosed; this fires as
    # well when the tracker itself has desynchronised, which is the case worth hearing
    # about.
    for name, open_blocks in depth.items():
        if open_blocks:
            violations.append(
                Violation(
                    md,
                    len(lines),
                    f"unclosed-{name}",
                    f"{open_blocks} {name} block(s) still open at end of file; give every "
                    f"{marker_form(name)} a matching close marker",
                    "",
                )
            )

    return violations


def check_handouts() -> list[str]:
    # Still a subprocess rather than a call into the imported module: --check has to
    # compare what a *fresh* run writes against what is on disk, and the generator's
    # exit status and stderr are the contract this reports.
    gen = REPO_ROOT / "scripts" / "gen_handouts.py"
    proc = subprocess.run(
        [sys.executable, str(gen), "--check"], capture_output=True, text=True
    )
    if proc.returncode == 0:
        return []
    return [line for line in (proc.stdout + proc.stderr).splitlines() if line.strip()]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--list", action="store_true", help="print the config and exit")
    args = ap.parse_args()

    if args.list:
        print(f"path keys:   {', '.join(PATH_KEYS) or '(none)'}")
        print(f"page marker: {PAGE_PATH_KEY}")
        print(f"markers:     {', '.join(marker_form(n) for n in BLOCK_DELIMS)}")
        print("tokens:")
        for label, token in PATH_TOKENS:
            print(f"  {label:26} {token.pattern}")
        print(f"allowlist:   {len(ALLOWLIST)} entries")
        for entry in ALLOWLIST:
            print(f"  {entry['file'] or '<any>':28} {entry['match'][:40]!r} -- {entry['why']}")
        return 0

    violations: list[Violation] = []
    pages = content_pages()
    for md in pages:
        violations.extend(lint_page(md))

    stale = check_handouts()

    for v in violations:
        print(str(v), file=sys.stderr)
    if stale:
        print("[stale-handouts] generated handouts do not match the source pages:", file=sys.stderr)
        for line in stale:
            print(f"    {line}", file=sys.stderr)

    if violations or stale:
        print(
            f"\nlint_paths: {len(violations)} violation(s) in {len(pages)} page(s)"
            + (", handouts stale" if stale else ""),
            file=sys.stderr,
        )
        return 1

    print(f"lint_paths: clean ({len(pages)} pages, handouts up to date)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
