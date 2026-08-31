# CLAUDE.md — UserRepo

> Global preferences (planning workflow, code quality, operations): `~/.claude/CLAUDE.md`
> Ecosystem: CentralRepo (Hugo container + theme), ctf_api (quiz engine), TEC-analytics (analytics platform), UserRepo (this repo).

## Project in One Line

The FortinetCloudCSE workshop **template**: the site every new workshop repo is cloned from, the authoring guide team members read, and the first repo a CentralRepo layout/shortcode change is proven against.

## It is a template — that is the constraint that governs everything

**Anything committed here is inherited by every new workshop repo.** Before adding a site-wide setting, a content page, or a `scripts/repoConfig.json` key, ask whether a workshop that has never heard of the feature should start life carrying it. If the answer is no, scope it to the page that demonstrates it.

Worked example: the deployment-path gate's live demo declares its two example paths in `content/02Hugo/6_deployment_paths/index.md` **front matter**, not as a `deploymentPaths` site param. Front matter gates that page alone and leaves when the page is deleted; a site param would have handed every new workshop two paths named *(example)* and a padlock line on every page. Declaring both at once is a hard build error. See the CentralRepo `CLAUDE.md` gate section.

## Stack Quick Reference

| Layer | Tech | Notes |
|-------|------|-------|
| Site generator | Hugo, inside `public.ecr.aws/k4n6m5h8/fortinet-hugo:latest` | No local Hugo install path — see Build below |
| Theme, layouts, config | [CentralRepo](https://github.com/FortinetCloudCSE/CentralRepo) | Mounted at build time; **not** in this repo |
| Deploy | `.github/workflows/static.yml` → GitHub Pages | Push to `main`, plus `workflow_dispatch` (`runner_type`, `image_variant` prod/dev) |
| Commit status | `Jenkinsfile` | Sets `ci/jenkins/build-status` only |
| Scanners | `lacework-code-security-pr.yml`, `codex-advisory-review.yml`, `fdevsec.yaml` | Lacework's two statuses take 3–5 min on every PR |

## Key Files

```
content/                  — the authoring guide, one page bundle per task, ordered by `weight`
layouts/shortcodes/       — repo-local shortcodes only: ContainerFlow, FTNThugoFlow, fortihugorunner
scripts/repoConfig.json   — the site-chrome knob: title, author, banner, theme variant, shortcuts
Jenkinsfile               — commit status; its content-check stage is disabled
repo_upgrade_spec.json / .repo_upgrade_version  — CentralRepo batch-migration bookkeeping
migration_log*.csv        — stale artifacts, and not even about this repo. Never treat as input.
```

No `hugo.toml`, `config.toml`, `Dockerfile`, `static/` or `docs/` here, on purpose.

## Build and Run

```bash
# Reproduce the CI build exactly
docker run --rm -v "$PWD:/home/UserRepo" public.ecr.aws/k4n6m5h8/fortinet-hugo:latest build

# Live preview
fortihugorunner launch-server --docker-image fortinet-hugo:latest \
  --host-port 1313 --container-port 1313 --watch-dir .
```

There is no test suite; content is validated by rendering. `npm install && hugo serve` does **not** work — Hugo's config lives in CentralRepo, and `package.json`'s `hugo` script references a `config.toml` and `docs/` that no longer exist.

## Gotchas

- **`docs/` is machine-owned — never put anything there.** `.gitignore` excludes it, *and* `CentralRepo/scripts/batch_repo_update.py` hardcodes `FOLDERS_TO_DELETE = ["docs"]` with `BRANCH = "main"`, deleting every blob under it via the GitHub tree API and pushing straight to `main`. That script does not read `repo_upgrade_spec.json`, so the spec and the constant can silently drift; the constant is what runs.
- **`.github/workflows/static.yml` is template-managed.** `batch_repo_update.py` overwrites it from the operator's CentralRepo checkout — hand-edits are lost. The same run deletes `layouts/shortcodes/FTNThugoFlow.html`, `docker-compose.yml`, `hugo.toml`, `config.toml` and `scripts/docker_*.sh`.
- **`package.json` and `package-lock.json` are listed in `.gitignore` but tracked** (they predate the entries). An ignore rule here is not evidence a file is untracked.
- **This repo forbids both squash and merge commits.** `gh-merge-verify <pr> --repo FortinetCloudCSE/UserRepo --method rebase` is the only strategy that works.
- **A brand-new branch with a PR opened immediately after its first push never gets a `ci/jenkins/build-status` check — it blocks merge forever, not just until CI runs.** Jenkins's webhook here only sends `push` events (no `pull_request`), and its multibranch job skips branches that already have an open PR — so nothing ever triggers a build for that SHA. `mergeStateStatus: BLOCKED` with an empty `reviewDecision` and no pending checks is this, not a review requirement (branch protection here requires 0 approvals). Confirmed 2026-08-31, PR #82. Not fixed at the infra level — see memory `gotcha_jenkins_webhook_push_only_pr_gap.md` for the workaround (temporarily drop the required check from branch protection, merge, restore it — needs admin + explicit sign-off, since it's a shared-repo settings change).
- **Change site chrome in `scripts/repoConfig.json`**, never in content — there is no `hugo.toml` to edit.
- **Repo-local `layouts/` wins over the container's** via `local_copy.sh`. Never land a copy of a CentralRepo shortcode here: the local one shadows it silently and the two drift.
- **Built page URLs are flat** — `02hugo/6_deployment_paths.html`, not `.../index.html`. Verification greps that assume a directory index find nothing.
- **Hugo minifies attributes unquoted** in built output (`class=pathgate data-path=docker`). Grepping for `data-path="docker"` returns zero on markup that is present.
- **`scripts/{gen_handouts,lint_paths}.py` and `.github/workflows/{path-lint,handout-pdf}.yml` sit inert in this repo** — they're ai-101's printable-handout tooling, copied in so every new workshop gets it for free; nothing runs until `deploymentPaths` is declared. See `content/02Hugo/7_printable_handouts/index.md`.
- **Before making `lint` or `handouts` a required status check in a repo that adopts this tooling, confirm their `pull_request` triggers still have no `paths:` filter.** A required check whose trigger is path-filtered never reports at all for a PR outside that filter, which blocks merge forever, not just until CI runs — bit `ai-101` the same day its own copies were made required. Already fixed in the copies here (both triggers are unfiltered; the equivalent filtering happens inside each job so a no-op PR still gets a fast, reporting green check).
