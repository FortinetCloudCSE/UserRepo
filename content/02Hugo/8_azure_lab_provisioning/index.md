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
2. **Idle, checked in, no attempt yet:** button reads "Provision Accounts" and is clickable.
3. **In flight:** the button disables (permanently, for this lab, until a terminal state), a progress bar fills, and a step label updates every few seconds — e.g. "Creating AD user — 20%", "Assigning role — 60%".
4. **On success:** a credential card renders in place — username, sign-in info, resource group, expiry, and an "Open Azure Portal" link — and the button reads "Already Provisioned" and stays disabled.
5. **On failure:** the button re-enables as "Retry Provisioning" and the status line shows the participant-safe failure reason from the backend.
6. **Reload or return later in the same browser session:** the page reads its stored state first — it resumes polling an in-flight attempt, or renders the stored credential card directly — before ever showing the plain "Provision Accounts" button. Closing the tab and coming back **the next day** starts fresh: state is `sessionStorage`, not `localStorage`, on purpose.

### Gotchas

- **Attempt state is scoped per Hugo site *and* per `lab`**, not just per site. Two `launchdemoform` shortcodes with different `lab` values on the same or different pages of the same workshop track independent attempts; the same `lab` value anywhere on the site shares one lock. Scoping is keyed on the reader's browser session (`sessionStorage`), prefixed with the site's own base URL — a participant working two different workshop sites in the same browser tab never sees one site's credentials or lock state on another.
- **The client-side single-attempt lock is a UX convenience, not the source of truth.** The backend's own idempotency (a deterministic key over participant email + lab definition + source site) is what actually prevents double-provisioning — this matters if you're debugging what looks like a stuck lock: clearing `sessionStorage` only resets what this *browser* remembers, not what the backend already did.
- **Retry only appears after a hard `Failed` status from the backend**, never just because a poll is slow or a tab was closed mid-provisioning. If a participant reports "it's been stuck at X% forever," that's a backend-side question (check the Function's Application Insights traces via the token), not a reason to expect a retry button to appear.
- **A missing or unreachable `provisionApiBaseUrl` fails safely.** No value configured → the shortcode never attempts a network call and shows the "not configured" message on click. A value that's set but wrong (typo, backend down) surfaces as a normal `Failed` attempt with a generic network-error reason, and the retry button appears once the URL is fixed.
- **This shortcode has no default backend URL any more.** The previous version silently posted to a hardcoded Azure Automation webhook if `site.Params.webhookUrl` wasn't set — and due to a separate bug, that site param was never actually wired into `hugo.toml` by `generate_toml.py`/`hugo.jinja`, so every real build used the hardcoded default regardless of what a repo configured. `provisionApiBaseUrl` is wired through the schema, the Jinja template, and `hugo.toml` generation, and has no hardcoded fallback — an unset value is a deliberate, visible "not configured" state instead of a silent default.

### Reference

- Shortcode source: [`layouts/shortcodes/launchdemoform.html`](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/layouts/shortcodes/launchdemoform.html) (CentralRepo)
- Backend API, lab-definition schema, and deployment: [`fortinet-on-demand-labs-provisioning-and-tracking`](https://github.com/FortinetCloudCSE/fortinet-on-demand-labs-provisioning-and-tracking)
- Site params reference: [CentralRepo README](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/README.md#site-params-referenced)
- Check-in cookies this shortcode depends on: [Analytics check-in](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/layouts/partials/analytics_checkin.html)
