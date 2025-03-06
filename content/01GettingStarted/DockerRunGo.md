---
title: "Go CLI Tool"
linkTitle: "Go CLI Tool"
weight: 3
---

The [docker-run-go](https://github.com/FortinetCloudCSE/docker-run-go/) CLI tool is a helper CLI tool that currently supports simplified workshop authoring on any Windows, MacOS, or Linux system with the following capabilities:

* Same usage across different development platforms
* Creates (builds) Fortinet Cloud CSE Docker development images
* Launches local Docker container with Hugo web server and live updating view of rendered site as modifications are made and saved

You can download the binary for your OS and architecture specifications from the repo. Binaries are available for Windows, Mac, and Linux. The following commands will help you determine your system architecture.


### System Architecture determination and binary download

{{< tabs groupid="a" >}}
{{% tab title="Windows" %}}
Run this command to find your OS Architecture 
```shell
C:\\wmic os get OSArchitecture
```

Depending on your output, download the appropriate Go Binary:
- [x86_64](https://github.com/FortinetCloudCSE/docker-run-go/raw/refs/heads/main/binaries/docker-run-go-windows-386.exe)
- [i386 or i686](https://github.com/FortinetCloudCSE/docker-run-go/raw/refs/heads/main/binaries/docker-run-go-windows-amd64.exe)
{{% /tab %}}
{{% tab title="MacOS/Linux" %}}
Run the following to get your OS Architecture:

```shell
> uname -m
```

Depending on the output, download the appropriate Go Binary:
- [MacOS aarch64](https://github.com/FortinetCloudCSE/docker-run-go/raw/refs/heads/main/binaries/docker-run-go-mac-amd64)
- [MacOS arm71](https://github.com/FortinetCloudCSE/docker-run-go/raw/refs/heads/main/binaries/docker-run-go-mac-arm64)
- [Linux aarch64](https://github.com/FortinetCloudCSE/docker-run-go/raw/refs/heads/main/binaries/docker-run-go-linux-amd64)
- [Linux arm71](https://github.com/FortinetCloudCSE/docker-run-go/raw/refs/heads/main/binaries/docker-run-go-linux-arm64)
{{% /tab %}}
{{< /tabs >}}

### Running the utility

Once the binary is downloaded, you can either run it from your workshop directory, or (recommended) copy it into your system path. If you copy it into your system path, it will be available throughout your system and you won't need to copy the binary anywhere else to run it.

{{< tabs groupid="a" >}}
{{% tab title="Windows" %}}

To find your system path on Windows:

```shell
C:\\echo %PATH%
``` 

Output:

```shell
C:\Windows\system32;C:Windows;C:\Program Files; .....
```

To copy the binary into your system path, choose a location listed, and move it there:

```shell
C:\\move docker-run-go-windows-amd64.exe "C:\Program Files"
```
{{% /tab %}}
{{% tab title="MacOS/Linux" %}}

To find your system path on Linux or MacOS:

```shell
> echo $PATH
```
{{% /tab %}}
{{< /tabs >}}
