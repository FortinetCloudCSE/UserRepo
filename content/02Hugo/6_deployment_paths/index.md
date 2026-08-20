---
title: "Task 6 - Deployment Paths (the choice gate)"
linkTitle: "Deployment Paths"
chapter: false
weight: 60
description: "Show each participant only the deployment path they chose — Docker, Kubernetes, cloud, whatever your workshop offers — instead of putting every variant on the same page."
# Declared here rather than in scripts/repoConfig.json on purpose: this repo is
# cloned to start every new workshop, and a site param would hand every new repo
# a path vocabulary it never asked for. Front matter scopes the live example to
# this page, and it leaves with the page.
deploymentPaths:
  - key: docker
    title: Docker Compose (example)
  - key: k8s
    title: Kubernetes / Helm (example)
---

### The problem this solves

If your workshop can be completed two ways — Docker Compose *or* Kubernetes, AWS *or* Azure, CLI *or* GUI — the obvious thing to do is put both on the page, side by side in tabs.

Participants then do **both**. Not some of them: enough of them that it is the single most common way a follow-along workshop goes wrong. Both sets of commands are visible, both look like steps, so both get run.

The **deployment path** feature fixes that by making the choice once, up front, and then showing that participant only their own path — in the page body, in the left-hand menu, in the next/previous buttons, and in search results.

{{% notice style="note" title="Opt-in — nothing changes until you ask for it" %}}
A workshop that declares no `deploymentPaths` behaves exactly as it always has: no extra markup, no CSS, no JavaScript on any page. There is no default path vocabulary and no repo inherits another repo's paths.

This page declares two example paths **in its own front matter**, so the feature is live on this page only — the controls above the title are real, and [the working example](#try-it) further down is gated by them. Every other page of this guide is untouched.
{{% /notice %}}

### Do you need it?

Use it when the **same learning objective** is reached by two or more mutually exclusive routes, and a participant only ever follows one.

| Situation | Use paths? |
|---|---|
| Docker Compose vs Kubernetes/Helm deployment of the same lab | **Yes** |
| AWS vs Azure vs GCP versions of the same exercise | **Yes** |
| "Advanced participants can also try…" — extra, optional material | No — that is a `notice` or an expander |
| Two different products covered in sequence | No — those are chapters |
| Showing the same command's output on Linux and macOS | No — that is a normal `tabs` block |

The test: if a participant should run **exactly one** of the variants and the other is *wrong* for them, use paths. If they might read both, use `tabs`.

---

### Step 1 — declare your paths

Declare the vocabulary in **one** of two places. Which one you pick decides how far the gate reaches.

#### The whole workshop is gated — `scripts/repoConfig.json`

This is the normal case. Add `deploymentPaths` as a site param:

```json
  "deploymentPaths": [
    { "key": "docker", "title": "Docker Compose" },
    { "key": "k8s",    "title": "Kubernetes / Helm" }
  ],
```

The participant chooses once and **every** page follows it: gated blocks, the left-hand menu, the next/previous buttons, search results, and a padlock line on every page so the choice is always visible and reversible.

#### One page gates itself — page front matter

Put the same list in a single page's front matter instead:

```yaml
deploymentPaths:
  - key: docker
    title: Docker Compose
  - key: k8s
    title: Kubernetes / Helm
```

Now only that page gates anything. No menu entry is hidden, no next/previous button is filtered, search is untouched, and the padlock line appears on that page alone. Reach for this when one page forks and the rest of the workshop does not — or when a page needs a self-contained demonstration, which is exactly what [the example on this page](#try-it) is.

Either way, each entry needs:

- **`key`** — the short identifier you will write in your markdown (`path="docker"`). Must start with a letter and contain only letters, digits, hyphens and underscores; it is used as part of a CSS class name as well as an attribute value.
- **`title`** — the label participants see on the button and in the "you are on this path" banner. Write it the way you want it read: **"Kubernetes / Helm"**, not `k8s`.

Two or more entries is the normal case. There is no limit, but every path multiplies the content you have to write and keep correct — two is almost always the right answer.

{{% notice style="note" title="Never both at once" %}}
Declaring `deploymentPaths` in a page's front matter while the site param also exists is a hard build error. There is one stored choice per participant per site, so the page would write its own key into the slot every site-wide page reads back — and those pages would then quietly show nothing at all, which is also what they correctly do before a first choice. Nothing would look broken.

`deploymentPath` (singular, the front-matter param that scopes a whole page to one path) is a different thing and needs the **site** param, because what it gates — menu, next/previous, search — is site-wide by definition.
{{% /notice %}}

{{% notice style="warning" title="Order and titles are both load-bearing" %}}
- The **first** entry is the default: it is the path shown to a participant with JavaScript disabled, and it is the tab the site marks active before anyone clicks. Prefer *appending* a new path over reordering the list.
- **Renaming a `title` silently resets every returning participant's choice** — the stored selection is keyed on the title text, so old selections stop matching. No build error, no warning; they are simply asked to choose again.
- **Renaming a `key` is the loud kind of change:** every `path="…"` in your markdown must be updated to match, or the build fails with a clear error. That is the safer of the two to get wrong.
{{% /notice %}}

---

### Step 2 — pick the right block for the job

There are three ways to scope content to a path. Use the smallest one that fits.

#### `pathtabs` / `pathtab` — parallel steps in the middle of a page {#pathtabs-block}

For a section where each path has its own version of the *same* step. The outer `pathtabs` block wraps one `pathtab` per path:

````markdown
{{</* pathtabs title="Deploy the stack" */>}}
{{%/* pathtab path="docker" */%}}
Bring the stack up on your own machine:

```bash
docker compose up -d
```
{{%/* /pathtab */%}}
{{%/* pathtab path="k8s" */%}}
Install the chart into your cluster:

```bash
helm upgrade --install mylab ./chart
```
{{%/* /pathtab */%}}
{{</* /pathtabs */>}}
````

- `title` is optional (default: *Your path*). It labels the banner that tells the participant which path they are on.
- Use `{{</* pathtabs */>}}` with angle brackets for the **outer** block, and `{{%/* pathtab */%}}` with percent signs for **each path's body** — the percent form is what renders the markdown inside.
- Every path in `deploymentPaths` must appear exactly once in every `pathtabs` block. This is enforced; see [what the build refuses](#what-the-build-refuses) below.

#### `pathonly` — one path, no tab UI

For prose, a warning, or a whole section that only applies to one path and has no counterpart on the other. Nothing is shown to the other path, and no tab strip is drawn:

```markdown
{{%/* pathonly path="k8s" */%}}
Your cluster needs a default StorageClass before you continue. Check with
`kubectl get storageclass`.
{{%/* /pathonly */%}}
```

{{% notice style="warning" title="`pathonly` must use the percent form" %}}
Write `{{%/* pathonly */%}}`, never `{{</* pathonly */>}}`. With angle brackets, any heading inside the block never joins the page's list of headings, so every in-page link to it breaks — silently, with no build error.

Leave a **blank line** above and below the opening and closing tags. Without them the markdown inside is treated as raw HTML and never rendered.
{{% /notice %}}

#### `deploymentPath` front matter — a whole page for one path

When an entire page belongs to one path, scope the page instead of wrapping its body. Add one line to the front matter:

```yaml
---
title: "Kubernetes / Helm Setup"
linkTitle: "Kubernetes / Helm"
weight: 20
deploymentPath: k8s
---
```

That single line does four things automatically:

1. Hides the page's entry in the **left-hand menu** for participants on another path.
2. Skips the page in the **next/previous** buttons, so following the arrows never walks into the other path.
3. Removes the page from **search results** for participants on another path.
4. If someone reaches it anyway — a bookmark, a shared link, a search from before they chose — shows a banner at the top explaining that the page belongs to the other path, with a button to switch.

Pair it with an opening `notice` that links to the equivalent page on the other path, so a participant who lands there has somewhere to go.

---

### What the participant sees

**Before choosing**, at the very top of any page that gates content — above the page title:

> **Choose your deployment path**
> *This page's steps are hidden until you pick one. Every other page then follows the same choice, and you can switch at any time from the header.*
> [ Docker Compose ] [ Kubernetes / Helm ]

The gated steps below stay hidden until they click. That is deliberate — it is the whole point — but it means **anything a participant needs in order to decide must live outside a path block.** Requirements, comparisons, "choose this if…" guidance: put those in plain page content, above the blocks.

**After choosing**, the buttons are replaced by a padlock line naming their path with a **Switch to …** button beside it. With a site-wide declaration that line appears on **every** page, so the choice is always visible and always reversible; with a page-level declaration it appears on the declaring page only, which is the only page the choice affects.

{{% notice style="tip" title="Tell them the buttons are buttons" %}}
Participants read documentation, not interfaces. Add a short notice near the top of your first page saying that the controls above the title are clickable and that the choice can be changed at any time from any page. It costs three lines and saves the "where did the Kubernetes steps go?" question.
{{% /notice %}}

**With JavaScript disabled**, every path is shown, labelled, with a note that they are alternatives rather than a sequence. Nothing is lost — the gate degrades to the old behaviour.

---

### Try it — this page is the example {#try-it}

Everything below this line is a real, working gate. It is driven entirely by this page's own front matter — nothing in `scripts/repoConfig.json`:

```yaml
deploymentPaths:
  - key: docker
    title: Docker Compose (example)
  - key: k8s
    title: Kubernetes / Helm (example)
```

That is the only configuration involved, and it is why the rest of this guide has no padlock line, no hidden menu entries and no gate markup at all. The markdown that produces the block below is exactly the escaped `pathtabs` example from [Step 2](#pathtabs-block), with the `/*` `*/` escapes removed.

{{< pathtabs title="Deploy the stack" >}}
{{% pathtab path="docker" %}}
You are reading the **Docker Compose** version of this step. A participant on the Kubernetes path never sees it.

```bash
docker compose up -d
```
{{% /pathtab %}}
{{% pathtab path="k8s" %}}
You are reading the **Kubernetes / Helm** version of this step. A participant on the Docker Compose path never sees it.

```bash
helm upgrade --install mylab ./chart
```
{{% /pathtab %}}
{{< /pathtabs >}}

And a `pathonly` block, which has no counterpart on the other path and draws no tab strip at all — on the Docker Compose path there is simply nothing here:

{{% pathonly path="k8s" %}}
**Kubernetes path only.** Your cluster needs a default StorageClass before you continue. Check with `kubectl get storageclass`. Nobody on the Docker Compose path is shown this paragraph, and no empty panel is left behind where it would have been.
{{% /pathonly %}}

Three things to notice while you are here:

- **The chooser is above the page title, not next to the blocks.** Scroll up. That is where every participant makes the choice, which is why the guidance they need to choose has to sit in plain page content.
- **The padlock line and its *Switch to …* button are on this page only.** Click through to another task and look above the title: nothing. That is the page-level declaration at work — a site-wide declaration would put that line on every page, which is what a real two-path workshop wants and what a guide like this one does not.
- **The rest of this page never changed.** Only the two blocks above are gated; ungated content is unaffected by the choice.

{{% notice style="tip" title="Starting a new workshop from this template? You inherit nothing" %}}
This repo is cloned to start every new workshop, which is the whole reason the example lives in front matter. `scripts/repoConfig.json` declares no paths, so a fresh clone has the feature switched off — delete this page and the example goes with it.

Had the example been a site param instead, every new workshop would have started life with two paths called *(example)* and a padlock line on every page.
{{% /notice %}}

---

### Editing existing blocks

#### Add a path to a workshop that already has two

1. Append the new entry to `deploymentPaths` — append, don't reorder.
2. Add a matching `pathtab` to **every** `pathtabs` block in the repo. The build fails, by design, listing each block that is missing the new path.
3. Review every `pathonly` block and every page with `deploymentPath` front matter: content that used to mean "not the other path" may now be wrong for the third one.
4. Check anything that hardcodes your path list — scripts, workflows, generated handouts. Derive it from `repoConfig.json` instead.

#### Remove a path

Delete its entry from `deploymentPaths` first, then build: every stale `path="…"` becomes a build error naming the file, which is your to-do list. Delete the orphaned `pathtab` bodies and any pages scoped to that path.

#### Convert an existing `tabs` block into a gated one

Rename the wrapper `tabs` → `pathtabs`, rename each `tab` → `pathtab`, and replace `title="…"` on each tab with `path="<key>"`. The tab titles now come from `deploymentPaths`, so they are consistent across every block in the workshop instead of being retyped per page.

#### Move content out of a block

The most common edit, and the most common mistake. Anything that is **true for everyone** — the explanation of *why* a step exists, a diagram, a link to reference material — should sit outside the path blocks. Content inside a block is invisible to participants on other paths and to anyone who has not chosen yet.

Rule of thumb: **inside the block, only the commands and the words that differ.** Everything else moves out.

#### Split a long page by path

If a page's two variants have diverged past the point where tabs read well, promote each variant to its own page with `deploymentPath` front matter and let the menu and next/previous gating do the work. That is usually the right move for setup and prerequisite pages, which tend to diverge most.

---

### What the build refuses {#what-the-build-refuses}

These are hard build failures, not warnings. Each one exists because the alternative is a silent gate that shows the wrong path's steps — which nobody notices until a participant does.

| The build fails when | Why |
|---|---|
| `pathtabs`, `pathtab` or `pathonly` is used with no `deploymentPaths` in either place | There is no path vocabulary to gate against, and no default to fall back on |
| A page declares `deploymentPaths` in front matter while the site param also exists | Two vocabularies behind one stored choice: the page's key would be written into the slot every site-wide page reads, and those pages would show nothing while looking correct |
| A `pathtabs` block is missing one of the configured paths | A participant on the missing path would silently be shown another path's steps |
| A `pathtabs` block defines the same path twice | Ambiguous — only one of them can win |
| A `pathtab` or `pathonly` body is empty | Renders an empty gated panel, which reads as "this path has nothing to do" rather than as the authoring mistake it is |
| `path="…"` names a key that is not in `deploymentPaths` | Typo; the error lists the valid keys |
| A `pathtab` sits outside a `pathtabs` block | Its content would never be collected or gated |
| A `pathonly` is nested inside `pathtabs`/`pathonly` | The enclosing block already restricts the path, so it is redundant or unreachable |
| A page's `deploymentPath` names an unknown key | The page would be hidden from *every* participant's menu |
| A page combines `deploymentPath` with `menuPageRef` or `menuUrl` | Those make the menu entry a crosslink, so the menu-hiding rule would match nothing and the page would stay visible to everyone with no error |
| A `key` does not start with a letter, or contains anything but letters, digits, hyphens and underscores | It becomes part of a CSS class name, so anything else silently produces a selector that never matches |

Every message names the offending file. Fix the file it names.

---

### Gotchas worth knowing up front

- **Put decision-making information outside path blocks.** If the prerequisites for each path live inside that path's `pathtab`, a participant who has not chosen yet can see *neither* — the information they need to choose is hidden behind the choice.
- **If a page now opens with a `notice`, set `description:` in its front matter.** Otherwise the site builds the page's description, its link previews, and its search snippet out of that notice's text.
- **A page scoped with `deploymentPath` is still reachable.** Menu and next/previous gating cannot stop a bookmark or a shared link. The banner covers this — but it is another reason to keep an opening `notice` that points at the other path's page.
- **Don't hardcode your path list anywhere else.** The `deploymentPaths` declaration is the single source. Scripts and workflows that need the list should read it from there, or they will quietly keep working with a stale list after you add a path. [Printable handouts](/02Hugo/7_printable_handouts/) is a worked example of exactly this — its generator derives everything from this same declaration.
- **With a site-wide declaration the switch control is site-wide, not per page.** A participant who picks wrongly on page one can fix it from any page — you do not need to repeat a chooser.
- **`deploymentPath` (singular) needs the site param.** Scoping a whole page to one path gates the menu, the next/previous walk and search, all of which are site-wide; a page-level `deploymentPaths` declaration deliberately touches none of them.

### Reference

- Shortcode parameters and site params: [CentralRepo README](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/README.md#shortcodes-and-usage)
- A live workshop using all three mechanisms: [ai-101](https://fortinetcloudcse.github.io/ai-101/) — see its `01Intro` chapter for the chooser, the comparison written outside the blocks, and two path-scoped prerequisite pages
- Printing a single path cleanly (the print-CSS gap this vocabulary feeds into): [Task 7 — Printable Handouts](/02Hugo/7_printable_handouts/)
