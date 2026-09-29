---
title: "Task 9 - Commands & Expected Output"
linkTitle: "Commands & Expected Output"
chapter: false
weight: 90
---

### Commands and expected output style

Use plain markdown code fences — no shortcode nesting. Follow this style for every
command/output pair:

- No `$` prompt in the command.
- One command per block, preceded by a sentence that says what it does.
- Introduce the output with "The output is similar to:".
- Use `[...]` for elided lines in long output.
- Reserve tabs for genuine alternatives (e.g. bash vs PowerShell) — not for hiding output.

### Which fence to use

Every block is a plain markdown fence — three backticks, an optional language, and optional
`{attributes}` in braces. Pick the fence by what the block *is*:

| Fence | Use it for | Attributes |
| ----- | ---------- | ---------- |
| ` ```bash `, ` ```sh `, ` ```shell ` | A command the reader runs | `run`, `title`, `label`, `icon`, `color` |
| ` ```text ` | A prompt typed into a chat UI (`run="chatbot"`), or any plain text | `run`, `title`, `label`, `icon`, `color` |
| ` ```output ` | What a command prints, or what the reader should see | `lang`, `hl_lines`, `collapse` |
| ` ```json `, ` ```yaml `, ` ```py `, … | Code or config quoted from a file | `title`, `wrap`, `lineNos` (Relearn's own) |
| ` ```` ` (four backticks) | Showing a fence itself, with its three backticks, in the text | none |

Rules that apply to all of them:

- Attribute values must be quoted: `{collapse="true"}`, not `{collapse=true}`. Hugo's fence
  parser rejects the bare form.
- Separate several attributes with a space: `{lang="json" collapse="true"}`.
- Nothing inside a fence is rendered as markdown or as a shortcode. `**bold**` and
  `{{</* colortext */>}}` show up literally. To draw attention to something in a block, see
  [Emphasising a line](#emphasising-a-line) below.
- Keep the content copy-safe: no `$` prompt, and no `<-- comments` inside a block the reader will copy.

### `run=` targets

Add `{run="<target>"}` to a `bash`, `sh`, `shell` or `text` fence to get a coloured
header badge. Five targets get a fixed colour and label — `bastion`, `local`, `pod`,
`browser` (each reads "Run on: &lt;Target&gt;") and `chatbot` (reads "Ask the chatbot",
see below); anything else gets a neutral badge.

Check the pods on the cluster:

```bash {run="bastion"}
kubectl get pods
```

The output is similar to:

```output
NAME                     READY   STATUS    RESTARTS   AGE
ollama-7d4f9c6b78-abcde  1/1     Running   0          4m
agent-6b8d5f9c7d-fghij   1/1     Running   0          4m
```

Run a command on your local machine:

```bash {run="local"}
docker ps
```

Exec into a pod:

```sh {run="pod"}
kubectl exec -it ollama-7d4f9c6b78-abcde -- /bin/sh
```

Open the app in a browser:

```shell {run="browser"}
open http://localhost:8080
```

An unrecognised target still renders, with a neutral badge:

```bash {run="jumphost"}
whoami
```

### `chatbot` blocks — for chat-UI prompts

`run=` also works on `text` fences, for prompts typed into a workshop's chat UI rather than
run in a shell. `chatbot` is a fifth standard target: header reads "Ask the chatbot" (not
"Run on: ..."), orange badge, FortiAI-Assist icon.

Enter this in the chat box:

```text {run="chatbot"}
Who is in the Engineering department?
```

### Custom label, icon and color

Every block's header text, icon and colour are author-editable, on any target, with the
`label`, `icon` and `color` attributes — for a one-off badge that isn't one of the five
standard targets:

```text {run="chatbot" label="Ask FortiAI-Assist" icon="fas fa-robot" color="#7a3fc4"}
Summarize this alert and recommend a remediation.
```

- `label` — replaces the header text entirely.
- `icon` — `terminal` (default for most targets), `fortiai` (the mark `chatbot` uses by
  default), or any Font Awesome class string, e.g. `fas fa-robot`.
- `color` — any CSS colour (hex, named, `rgb()`) for the header background.

### `output` fences

Plain output, no syntax colouring, no copy button:

```output
qwen2.5:3b
```

Optional `lang="json"` highlights inside the panel:

```output {lang="json"}
{
  "models": ["qwen2.5:3b"]
}
```

Optional `hl_lines="2"` puts a background band behind the listed lines, to point at the one
value the reader has to check. Quote it; a list or range such as `"1-2 4"` also works:

```output {hl_lines="2"}
NAME             STATUS   ROLES    AGE
aks-aiuser49     Ready    <none>   6m33s
```

Optional `collapse="true"` wraps long output in the theme's expand widget (the value must be
quoted — Hugo's fence-attribute parser does not accept a bare `collapse=true`):

```bash {run="bastion"}
kubectl describe pod ollama-7d4f9c6b78-abcde
```

The output is similar to:

```output {collapse="true"}
Name:         ollama-7d4f9c6b78-abcde
Namespace:    ai101
[...]
Status:       Running
```

Attributes combine, in any order: `{lang="json" hl_lines="2" collapse="true"}`. `hl_lines` needs
a build image that includes the feature; on an older image the attribute is silently ignored and
the block renders without the band.

### Emphasising a line

Because fences don't render markdown, use one of these instead:

- **`hl_lines`** on an `output` fence, for one line in the output (above).
- A bold sentence before the block: "The output must show **your cluster name**."
- A `notice` for something the reader must not skip. Never put quotes or `**bold**` in the
  notice title — Hugo fails the whole build with "Cannot mix named and positional parameters".
- `{{</* colortext "red" */>}}text{{</* /colortext */>}}` for coloured text in prose (not inside a fence).

### `title=` composes with `run=`

For a multi-command step, keep Relearn's `title` alongside the run-on badge:

```bash {run="bastion" title="Install the Helm chart"}
helm upgrade --install ai101 ./helm/ai101 -f values-lab1.yaml
```

### Fallback (no CentralRepo image needed)

If the `run=`/`output` render hooks aren't in the image you're building against yet,
this renders a titled block today with zero CentralRepo changes:

```bash {title="Run on: bastion"}
kubectl get pods
```

```text {title="Expected output"}
NAME   READY   STATUS
```
