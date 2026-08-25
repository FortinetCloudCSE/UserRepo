---
title: "Task 8 - Azure Lab Provisioning"
linkTitle: "Azure Lab Provisioning"
chapter: false
weight: 80
description: "Provision per-participant Azure lab accounts from a workshop page, with real progress, on-page credentials, and a single-attempt lock — no dependency on the confirmation email arriving in time."
---

### The problem this solves

Workshops that need per-participant Azure accounts (a resource group, a portal sign-in, sometimes a VM) use the `launchdemoform` shortcode (CentralRepo) to trigger provisioning. Until now, that button POSTed to an Azure Automation webhook using `mode:'no-cors'` — the request went out, but the response was opaque by design, so the page could never show real status. Credentials arrived by a single Gmail-SMTP email, which routinely didn't land in time for a live workshop.

`launchdemoform` now calls a real HTTP API (an Azure Durable Function, in [`fortinet-on-demand-labs-provisioning-and-tracking`](https://github.com/FortinetCloudCSE/fortinet-on-demand-labs-provisioning-and-tracking)) that returns a real, readable response and a status endpoint the page polls. Participants see a progress bar and step name while provisioning runs, and credentials render directly on the page the moment they're ready — email is now a secondary/audit channel, not the only delivery path.

{{% notice style="note" title="Only add this shortcode where Azure provisioning is actually required" %}}
`launchdemoform` should appear on labs that use this repo's Azure automation, and be **removed** from workshops that don't need it — it has no effect and shows nothing useful otherwise. It requires a participant to have already checked in (the `fortiuser`/`fortiemail` cookies come from the site's analytics check-in flow, unchanged by this feature).
{{% /notice %}}

### Params

Shortcode params (unchanged by this rework):

| Param | Required | Meaning |
|---|---|---|
| `lab` (or `labdefinition`) | Yes | The lab definition to provision — matches a file name (minus `.json`) under [`lab-definitions/`](https://github.com/FortinetCloudCSE/fortinet-on-demand-labs-provisioning-and-tracking/tree/main/lab-definitions) in the backend repo, e.g. `azure-102-odl`. |
| `debug` | No, default `false` | `true` logs request/response/state-transition detail to the browser console. |
| `customer` | No | Optional customer identifier passed through to the backend. |
| `smartticket` | No | Optional SmartTicket reference passed through to the backend. |

One new **site param**, in this repo's `scripts/repoConfig.json`:

```json
  "provisionApiBaseUrl": "https://<your-function-app>.azurewebsites.net"
```

Point it at the deployed Function App from the backend repo. **Leave it unset until that Function is actually deployed and reachable** — with no value, the shortcode renders normally (the button is still gated on check-in as before) but a click shows a clear "Provisioning is not configured for this workshop yet" message instead of failing against a URL that doesn't exist.

### Usage

````markdown
{{</* launchdemoform lab="azure-102-odl" */>}}
````

### Live example

{{% notice style="tip" title="What you'll see here depends on your check-in/config state" %}}
This repo's own `scripts/repoConfig.json` intentionally has no `provisionApiBaseUrl` set — the example below is live, but clicking it (once you've checked in) demonstrates the "not configured" state rather than a real provisioning run. A workshop with the site param set and a real backend behaves as described in [What the participant sees](#what-the-participant-sees) below.
{{% /notice %}}

{{< launchdemoform lab="azure-102-odl" >}}

### What the participant sees {#what-the-participant-sees}

1. **Before checking in:** the button is disabled with a message to check in first (unchanged behavior).
2. **Idle, checked in, no attempt yet, no reusable credential found:** button reads "Provision Accounts" and is clickable.
3. **Idle, checked in, and a valid credential from an earlier workshop exists** — either the same lab-definition, or a different one tagged into the same `series` (see [Gotchas](#gotchas) below) — the plain button is replaced by a choice: "We found existing credentials from **{workshop}**, issued {date}" with two buttons:
   - **Reuse These Credentials** — renders that credential immediately (username, TAP, resource group, a "Reused from" line naming the original workshop) with no new provisioning call at all.
   - **Provision New For This Workshop** — proceeds with the normal flow below as if no prior credential existed. This choice is remembered only for *this* page's site+lab, not the whole series — a different workshop page later in the same series still offers the reuse choice fresh.
4. **In flight:** the button disables (permanently, for this lab, until a terminal state), a progress bar fills, and a step label updates every few seconds — e.g. "Creating AD user — 20%", "Assigning role — 60%".
5. **On success:** a credential card renders in place — username, sign-in info, resource group, expiry, and an "Open Azure Portal" link — and the button reads "Already Provisioned" and stays disabled.
6. **On failure:** the button re-enables as "Retry Provisioning" and the status line shows the participant-safe failure reason from the backend.
7. **Reload, close the tab, or restart the browser — the page always reads its stored state first:** it resumes polling an in-flight attempt, or renders the stored credential card directly, before ever showing the plain "Provision Accounts" button. State is `localStorage`, not session-only — it survives tab/browser closure by design, since a provisioned credential is only valid for the lab's own duration regardless of how long a browser stays open. Once that duration has passed, the credential card still renders (as a record of what was issued) but shows an inline "access window has ended" warning instead of presenting a dead credential as still good.

### Gotchas

- **Attempt state is scoped per Hugo site *and* per `lab`**, not just per site. Two `launchdemoform` shortcodes with different `lab` values on the same or different pages of the same workshop track independent attempts; the same `lab` value anywhere on the site shares one lock. Scoping is keyed on the browser's `localStorage`, prefixed with the site's own base URL — a participant working two different workshop sites in the same browser never sees one site's credentials or lock state on another.
- **The client-side single-attempt lock is a UX convenience, not the source of truth.** The backend's own idempotency (a deterministic key over participant email + lab definition + source site) is what actually prevents double-provisioning, and it has no expiry of its own — this matters if you're debugging what looks like a stuck lock, or wondering why a participant can't start a genuinely new attempt after their lab access has ended: clearing `localStorage` only resets what this *browser* remembers, not what the backend already did. Getting a real new attempt for the same email+lab+site is a backend-side question, out of scope for anything client-side.
- **Retry only appears after a hard `Failed` status from the backend**, never just because a poll is slow or a tab was closed mid-provisioning. If a participant reports "it's been stuck at X% forever," that's a backend-side question (check the Function's Application Insights traces via the token), not a reason to expect a retry button to appear.
- **A missing or unreachable `provisionApiBaseUrl` fails safely.** No value configured → the shortcode never attempts a network call and shows the "not configured" message on click. A value that's set but wrong (typo, backend down) surfaces as a normal `Failed` attempt with a generic network-error reason, and the retry button appears once the URL is fixed.
- **Linking two workshops into a reusable credential "series" is a lab-definition change, not a shortcode param.** A participant who already completed one workshop can be offered their existing credential on a later one (see [What the participant sees](#what-the-participant-sees), step 3) when either (a) both workshops' `launchdemoform` calls use the *literal same* `lab` value (nothing to configure — this is how the K8s 101/201/202 trio works today), or (b) their lab-definitions are genuinely different but both set the same `series` string in the lab-definition JSON (in [`lab-definitions/`](https://github.com/FortinetCloudCSE/fortinet-on-demand-labs-provisioning-and-tracking/tree/main/lab-definitions) in the backend repo — not this repo). There's no shortcode-side setup: once the backend lab-definitions share a `series` (or are the same lab), the reuse choice appears automatically. Only identity (the AD user/TAP) is reused across a series — a linked workshop's own resource groups/storage/VM still provision fresh if it needs them.
- **This shortcode has no default backend URL any more.** The previous version silently posted to a hardcoded Azure Automation webhook if `site.Params.webhookUrl` wasn't set — and due to a separate bug, that site param was never actually wired into `hugo.toml` by `generate_toml.py`/`hugo.jinja`, so every real build used the hardcoded default regardless of what a repo configured. `provisionApiBaseUrl` is wired through the schema, the Jinja template, and `hugo.toml` generation, and has no hardcoded fallback — an unset value is a deliberate, visible "not configured" state instead of a silent default.

### Admin: logs, credential recovery, and troubleshooting {#admin-troubleshooting}

{{% notice style="warning" title="Azure Portal access required" %}}
Everything below is in the `Internal-Training` subscription, resource group `CloudCSE-WorkshopAccountProvisioning`. You need at least Reader on that resource group to follow along.
{{% /notice %}}

**The backend:** Function App `func-cse-lab-provisioning` (Python, Durable Functions, EP1 plan). Search for that exact name in the Azure Portal to get to everything else — its Function App blade links to its Application Insights resource and its own Durable Functions instance list.

**Every request is logged and correlatable by the orchestration instance ID** — which is also the `token` the shortcode polls `GET /api/provision/status/{token}` with, so it's visible in the participant's browser dev tools (Network tab) or console (`debug=true` shortcode param logs it directly). All logs land in Application Insights `appi-cse-lab-provisioning` (backed by Log Analytics workspace `appi-cse-lab-provisioning-law`, **30-day retention**). From the Function App blade → **Application Insights** → **Logs**, run:

```kql
traces
| where customDimensions.instance_id == "<token>"
| order by timestamp asc
```

This reconstructs the entire run for one participant — every step name, percent, and (on failure) the real exception with a stack trace, not just the generic participant-safe failure message the page shows. `log_failure` writes failures to `traces`/`exceptions` at `error` level; a stuck or failed provisioning is almost always diagnosable from this one query.

**Finding a participant's instance ID when you don't have it** (they lost the tab, the email never arrived, and they can't give you the token): the orchestration's stored *input* includes their email, but email is never logged into `customDimensions` directly, so `traces` can't be full-text-searched by email. Instead use the Durable Functions instance list — either the Function App's own **Durable Functions instances** view in the Portal, or the management REST API (`.../runtime/webhooks/durabletask/instances?showInput=true&showOutput=true`, auth code from the Function App's host keys) — and filter the results for `input.email`. This lists every orchestration regardless of terminal state, which is also the fastest way to answer "is this participant's attempt actually stuck, or did it fail/succeed and they just didn't see it."

**Fastest path: check the `Training Credentials` channel in the `Cloud Architects` Team first.** Every successful provisioning posts a formatted card — workshop name, participant email, username, password/TAP — to that Teams channel via a Power Automate webhook, at the same moment the participant's credential email goes out. This is the intended first stop for "a participant says they never got their credentials" — faster than any of the lookups below, since it needs no instance ID and no Portal access.

The webhook posts through a Power Automate flow (`fd0bf968c0df4299aa09ab673de41b04`, same Power Platform environment as `ManageTrainingUser.ps1`'s original webhook) — open it in [Power Automate](https://make.powerautomate.com/) if the destination ever needs to change.

This only covers labs that reach the `send_email` step successfully — a `Failed` attempt never posts (use the instance-ID/Application Insights lookups below for those), and the notification itself is best-effort: a webhook failure is logged (`step: teams_webhook`) but never blocks credential delivery or rolls back provisioning, so occasionally you'll need to fall back to the lookups below even for a `Completed` attempt.

**Recovering an already-issued credential** depends on which lab path ran:

- **Bastion + VM labs** (10 of 11 lab definitions): the VM's local-admin password is a durable Key Vault secret, `vm-password-<resource-group-name>`, in the dedicated vault `kv-cse-wksp-provision`. Look up the resource group name from the orchestration's output (same instance lookup as above), then read that secret directly — no time limit, it doesn't expire or get purged.
- **AD user / Temporary Access Pass labs** (`azure-102-odl` and similar): the TAP is **not** stored anywhere durable on purpose — it's a Microsoft Entra credential, emailed once and returned once in the orchestration's output. The orchestration's *output* (via the same instance-ID lookup, `show_output=true`) still has the original TAP value **as long as the Durable Task history hasn't been purged** — nothing currently purges it (no retention policy configured on the `ProvisioningTaskHub` storage), so in practice this works well past the 30-day Application Insights window. If the TAP has since expired (they're short-lived) or truly can't be found, don't try to reuse it — issue a fresh one for that user directly in Entra ID (**Users** → the participant's AD user → **Authentication methods** → **Temporary Access Pass**). The AD user itself persists across labs; only the TAP is single-use/time-boxed.

**Checking whether a participant is rate-limited or "stuck" on a stale lock:** the dedup/rate-limit state lives in a Durable Entity (`ProvisionEntity`), one instance per `email:<lowercased-email>` and one per `dedup_key` (email + lab + source site). Query entity state the same way as orchestration status (Durable Functions instance/entity list, entity ID `@ProvisionEntity@email:<email>` or `@ProvisionEntity@<dedup_key>`) if a participant reports the button won't let them retry — this tells you whether the backend genuinely still considers them in-flight/already-completed, independent of whatever the browser's `localStorage` shows.

{{% notice style="tip" title="Client-side state is not authoritative" %}}
Clearing a participant's browser `localStorage` (or having them use a different browser) never unblocks a real backend-side lock or rate limit — it only resets what their browser remembers. Always confirm against the Durable Entity state above before telling a participant to "just try a different browser."
{{% /notice %}}

**Tracing a reused credential (a participant says "it gave me someone else's/an old workshop's credentials"):** verify via the backend, never by guessing from what the page shows.

1. **Fastest check — the orchestration's own output.** Find the participant's instance ID the same way as above (Durable Functions instance list filtered on `input.email`), then read that instance's *output*. If the credential was reused, the output has a `reusedFrom` field naming the lab-definition the identity/TAP originally came from. No `reusedFrom` field means that specific attempt provisioned fresh — the participant's complaint is about a different attempt, or a client-side display bug, not the reuse mechanism.
2. **Full per-participant history** — every lab that email has ever completed, reused or not — lives in a separate Durable Entity, one instance per email, entity ID `history:<sha256 of the lowercased, trimmed email>` (hashed rather than the raw email — a `read_entity_state` HTTP lookup on a key containing `@` doesn't resolve; see this repo's backend `CLAUDE.md` if you're touching this code). Compute the key with:
   ```bash
   python3 -c "import hashlib; e='participant@example.com'.strip().lower(); print('history:' + hashlib.sha256(e.encode()).hexdigest())"
   ```
   Then look that entity up the same way as `ProvisionEntity` above (Durable Functions instance/entity list, `@ProvisionEntity@history:<hash>`). Its state is a list of every completion for that email — `lab_definition_name`, `series`, `user_principal_name`, `completed_at`, `lab_duration_days` — the authoritative record of what that participant actually has and where each credential came from.
3. **"It gave me an old workshop's credentials" almost always means the reuse was correct and expected** — the participant is confusing "the same account, still valid, from an earlier session today" with "wrong account." Confirm by checking `completed_at` + `lab_duration_days` on the matching history entry actually covers *now* (an expired-but-still-`Completed` entry is never offered for reuse server-side — see the backend README's "Credential reuse" section — so if they're seeing stale credentials from *outside* that window, that's a genuine bug, not the intended behavior, and worth escalating with the instance ID from step 1).

### Reference

- Shortcode source: [`layouts/shortcodes/launchdemoform.html`](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/layouts/shortcodes/launchdemoform.html) (CentralRepo)
- Backend API, lab-definition schema, and deployment: [`fortinet-on-demand-labs-provisioning-and-tracking`](https://github.com/FortinetCloudCSE/fortinet-on-demand-labs-provisioning-and-tracking)
- Credential reuse mechanism (`series` field, `GET /api/provision/lookup`, per-email history entity): backend README's ["Credential reuse"](https://github.com/FortinetCloudCSE/fortinet-on-demand-labs-provisioning-and-tracking#credential-reuse) section
- Backend logging helper (the `customDimensions.instance_id` correlation pattern): [`src/logging_utils.py`](https://github.com/FortinetCloudCSE/fortinet-on-demand-labs-provisioning-and-tracking/blob/azure-function-rebuild/src/logging_utils.py)
- Backend infra (Function App, Application Insights, Key Vault names): [`infra/main.bicep`](https://github.com/FortinetCloudCSE/fortinet-on-demand-labs-provisioning-and-tracking/blob/azure-function-rebuild/infra/main.bicep)
- Site params reference: [CentralRepo README](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/README.md#site-params-referenced)
- Check-in cookies this shortcode depends on: [Analytics check-in](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/layouts/partials/analytics_checkin.html)
