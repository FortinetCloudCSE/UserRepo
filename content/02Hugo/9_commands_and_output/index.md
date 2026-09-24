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

### `run=` targets

Add `{run="<target>"}` to a `bash`, `sh` or `shell` fence to get a coloured
**"Run on: &lt;Target&gt;"** header. Four targets get a fixed colour; anything else
gets a neutral badge.

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
