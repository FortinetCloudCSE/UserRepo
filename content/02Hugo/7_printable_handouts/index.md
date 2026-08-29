---
title: "Task 7 - Printable Handouts"
linkTitle: "Printable Handouts"
chapter: false
weight: 70
description: "Generate a single-path, print-safe handout for each deployment path — the print stylesheet only ever shows the active tab, so a tabbed page printed as-is silently drops the other path."
---

### The problem this solves

[Deployment paths](/02Hugo/6_deployment_paths/) show each participant only their own path in the browser: `pathtabs` renders one tab active, one hidden, and JavaScript swaps them on click. That is exactly what makes it useless on paper.

`theme.css` sets `.tab-content { display: none }` with `.tab-content.active { display: block }`. That is not a print-only rule — the print stylesheet only recolours tabs for the page, it does not un-hide anything. So a two-path page, printed or exported to PDF exactly as it renders, contains **one path's steps and zero indication the other path's steps ever existed.** No error, no missing-content notice — the page just looks complete. A participant who prints the Kubernetes path for offline reference silently gets a document with no `helm` commands, or vice versa.

The fix is not a print stylesheet — the tab that isn't active isn't in the printed DOM at all, so no `@media print` rule can recover it. The fix is a **separate, generated page per path**, flattened ahead of time so nothing needs to be hidden. That is what this tooling does.

{{% notice style="note" title="Opt-in — nothing changes until you ask for it" %}}
The same rule as [deployment paths](/02Hugo/6_deployment_paths/) itself: a workshop that declares no `deploymentPaths` gets no generated handouts, no extra CI time, and no `content/09Reference/handouts/` directory. All four files below already sit in this repo, inert, as of this change — see [How to opt in](#how-to-opt-in).
{{% /notice %}}

### The four files

| File | Job |
|---|---|
| `scripts/gen_handouts.py` | Walks `content/` in site order and, per deployment path, writes one linear page to `content/09Reference/handouts/` with every `pathtabs`/`pathonly`/`tabs` block flattened to that path's body and the other path's content dropped entirely — not collapsed, dropped, because collapsed is exactly the failure mode above. `--check` exits 1 if regenerating would change anything; `--list-slugs` prints the handout slugs and nothing else. |
| `scripts/lint_paths.py` | Guards the invariant the generator depends on: every path-specific instruction has to actually live inside a `pathtabs`/`pathonly` block (or a page-level `deploymentPath`) or the generator has no way to flatten it correctly. It imports its marker grammar and path vocabulary from `gen_handouts.py` rather than keeping a second copy. Its final check delegates to `gen_handouts.py --check` — a lint pass and a stale-handout are the same failure, reported together. |
| `.github/workflows/path-lint.yml` | Runs on every PR touching content: regenerates the handouts and fails loud if that produces a diff, then runs `lint_paths.py` — see [the CI gate](#the-ci-gate) below. On a push to `main` (never on a PR — see below), the auto-fix commits and pushes the regenerated handouts instead of just failing. |
| `.github/workflows/handout-pdf.yml` | Runs a full Hugo build, serves it, and renders each handout to PDF with headless Chrome. PR-triggered so a real build failure (the actual incident this hardening was built after — a bad `pathtabs` block that passed lint but broke the Hugo build) is visible **before** merge, reusing the build step this workflow already ran, rather than adding a third copy of build-and-fail-on-error. |

### How to opt in

Declare `deploymentPaths` — site-wide in `scripts/repoConfig.json`, or page-scoped in a single page's front matter — exactly as described in [Step 1 of the deployment-paths guide](/02Hugo/6_deployment_paths/#step-1--declare-your-paths). The moment a real path vocabulary exists:

- `gen_handouts.py` starts producing pages under `content/09Reference/handouts/`, one per path.
- `lint_paths.py` starts enforcing that every path-specific instruction sits inside a path block.
- Both workflows above stop short-circuiting and start doing real work on every PR.

Nothing else changes. `scripts/lint_paths.py`'s own `PATH_TITLE_RE`, `PATH_TOKENS` and `ALLOWLIST` are empty in this repo's copy — they carried ai-101's docker/kubectl/helm vocabulary, which is that workshop's content, not a generic default — so a repo that writes real path-specific lab content should repopulate them the way ai-101 did (see the comments at the top of `scripts/lint_paths.py` for the reuse recipe).

### The CI gate {#the-ci-gate}

"Stale" means the committed pages under `content/09Reference/handouts/` do not match what `gen_handouts.py` would write today — a source page changed and nobody re-ran the generator. `--check` (used by both `lint_paths.py` and `handout-pdf.yml`) catches this and fails loud, naming every changed and orphaned file.

`path-lint.yml` goes one step further, but **only on a push to `main`, never on a pull request** — before linting, it runs `gen_handouts.py` for real (not `--check`), and if that produces a diff, it commits and pushes the fix using a repo secret named `HANDOUT_AUTOFIX_PAT` — a fine-grained PAT (`contents: write`, scoped to that one repo), not the workflow's own `GITHUB_TOKEN`. That distinction matters: a push made with `GITHUB_TOKEN` deliberately does not re-trigger other workflow runs, so a re-run against the corrected head wouldn't happen automatically. The push is deliberately restricted to the `push` trigger: a `pull_request` run has just executed the PR head's own (potentially untrusted) `gen_handouts.py` in the same job, and GitHub Actions runner state persists across steps in one job — combining that with a secret capable of pushing to the repo is a real credential-exfiltration risk, not a theoretical one. So a PR that needs its handouts regenerated has to be fixed locally (`python3 scripts/gen_handouts.py` + commit) or merged and left to self-heal on `main` afterward — it is never auto-fixed *during* review.

**A repo without its own `HANDOUT_AUTOFIX_PAT` still gets the full safety guarantee — just not the auto-fix.** The push step checks the secret is present (and that the trigger is `push`) before attempting anything; if either isn't true, it reverts its own regeneration and leaves the stale files in place, and `lint_paths.py` fails with the same clear "handouts are stale, re-run `gen_handouts.py`" message it always has. Nothing pushes with an empty credential, nothing produces an opaque git-auth error — the mechanism degrades from self-healing to fail-loud-and-tell-you-how-to-fix-it, never to silently-wrong. This repo (`UserRepo`) does not provision the secret — there is nothing here to print — so this is the path every clone of this template actually exercises.

To get the auto-fix instead of just the fail-loud check, mint a fine-grained PAT the same way `ai-101` did — `contents: write`, scoped to that one repo only — and store it as a repository secret named `HANDOUT_AUTOFIX_PAT`.

### Live example

[**ai-101**](https://github.com/FortinetCloudCSE/ai-101) is the one workshop currently using this end to end: `deploymentPaths` declared site-wide, real `pathtabs` content throughout, `HANDOUT_AUTOFIX_PAT` provisioned, and its own `PATH_TITLE_RE`/`PATH_TOKENS`/`ALLOWLIST` populated with its docker/kubectl/helm vocabulary. Its [published handouts](https://fortinetcloudcse.github.io/ai-101/09reference/handouts/) are the generator's real output.

### Reference

- Deployment paths (the vocabulary this tooling reads): [Task 6](/02Hugo/6_deployment_paths/)
- A live workshop using the full mechanism: [ai-101](https://github.com/FortinetCloudCSE/ai-101)
