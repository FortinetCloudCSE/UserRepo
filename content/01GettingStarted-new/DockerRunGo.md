---
title: "Go CLI Tool"
linkTitle: "Go CLI Tool"
weight: 3
---

## New Go Utility for interacting with Container
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
os get OSArchitecture
```

Depending on your output, download the appropriate Go Binary from the [releases page](https://github.com/FortinetCloudCSE/docker-run-go/releases/)

{{% /tab %}}
{{% tab title="MacOS/Linux" %}}
Run the following to get your OS Architecture:

```shell
uname -m
```

Depending on the output, download the appropriate Go Binary from the [releases page](https://github.com/FortinetCloudCSE/docker-run-go/releases/):

{{% /tab %}}
{{< /tabs >}}

### Utility Setup

You should place the downloaded binary at the root of your Hugo development folder so it's in a **well-known location**.  This will make replacing and/or upgrading the utility easier.

{{% notice style="tip" title="For Example" %}}
If you use /home/ubuntu/pythonProjects/ for all of your Hugo development, and you clone repos into this folder structure, you should place the Go Utility here as your **well-known location**
{{% /notice %}}

Further, adding this **well-known location** to your system's $PATH will enable you to run the utility on any repo you edit.


{{< tabs groupid="a" >}}
{{% tab title="Windows" %}}
{{% notice style="tip" %}}
In the following examples, we'll use **C:\users\someUser\pythonProjects** as our **well-known-location**
{{% /notice %}}

{{< tabs >}}
{{% tab title="Windows CLI " %}}
To show and change your system path using Windows CLI do the following:
```shell
echo %PATH%
setx PATH "%PATH%;C:\users\someUser\pythonProjects"
echo %PATH%
``` 
{{% notice style="warning" %}}
The `echo %PATH%` command lists your existing $PATH variable before and after the `setx` change.  Be careful with `setx` as it replaces the `PATH` value, not appends (though `%PATH%` includes the existing value).
{{% /notice %}}
{{% /tab %}}
{{% tab title="Windows Powershell" %}}
To show and change your system path using Windows Powershell do the following:

```shell
$env:Path
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\users\someUser\pythonProjects", [EnvironmentVariableTarget]::User)
$env:Path
```

{{% /tab %}}
{{% /tabs %}}

{{% /tab %}}
{{% tab title="MacOS/Linux" %}}

To find your system path on Linux or MacOS:

```shell
echo $PATH
```

To add your **well-known-location** to the system path, edit the ```etc/environment``` file and append the **well-known location** for the Go Utility.  The following commands show you how to do this using nano editor:
{{% notice style="tip" %}}
In the following examples, we'll use **/home/ubuntu/pythonProjects** as our **well-known-location**
{{% /notice %}}

1. Open the File
    ```bash
    sudo nano etc/environment
    ```
2. Find the PATH line and append your **well-known location** where the Go Utility binary is stored, to the end of the existing line, making sure to retain the end <kbd>"</kbd>

    **append __/home/ubuntu/pythonProjects/__ to the end of the following line as so:**
    
    ```bash
    PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/ubuntu/pythonProjects/"
    ```
3. Save file and exit nano editor with: <kbd>CTRL</kbd>+<kbd>X</kbd>, then <kbd>Y</kbd>, then <kbd>Enter</kbd>
4. Apply the file changes to your current terminal session
    ```bash
    source /etc/environment
    ```
5. Verify the change
    ```bash 
    echo $PATH
    ```
   
6. Finally, make sure the Go Binary is executable:
   ```bash
   chmod +x /home/ubuntu/pythonProjects docker-run-go
   ```
{{% /tab %}}
{{< /tabs >}}

### Running the utility

Once the binary is downloaded, you can either run it from your workshop directory, or (recommended) copy it into your system path. If you copy it into your system path, it will be available throughout your system and you won't need to copy the binary anywhere else to run it.
You can use the following CLI arguments to modify the utility's behavior.  If you run the utility from an existing Hugo repo directory, leaving the CLI blank will run with defaults listed

General steps:
1. Run the Utility to **BUILD** your container.  This step is only necessary when we've added features or capabilities within the container.  Rebuilding pulls the latest/greatest into your container image
2. For Any repo you want to edit, run the utility with ```launch-server``` command to get a local live-updating view of your Hugo workshop site.

CLI options with defaults for **Container BUILD**
```shell
docker-run-go build-image \
    admin-dev       # testing image, used for container/process development, named ```hugo-tester```
    author-dev      # daily-use image for workshop authoring, named ```fortinet-hugo```
```

CLI Options with defaults for **Container RUN**
```shell
docker-run-go launch-server \
  --docker-image fortinet-hugo:latest \
  --host-port 1313 \
  --container-port 1313 \
  --watch-dir .
```

{{< tabs groupid="a" >}}
{{% tab title="Windows" %}}
1. Navigate to your workshop repo directory and run the utility (which is 1 level up in your development root/**well-known-location**).  
  - In the example below, we are working on UserRepo located at ```C:\users\someUser\pythonProjects\UserRepo```
2. Build the Docker image
3. Launch Hugo server in Author Mode

```shell
cd C:\users\someUser\pythonProjects\UserRepo
..\docker-run-go.exe build-image author-dev
..\docker-run-go.exe launch-server
```

{{% /tab %}}
{{% tab title="MacOS/Linux" %}}
1. Navigate to your workshop repo directory and run the utility (which is 1 level up in your development root/**well-known-location**).  
  - In the example below, we are working on UserRepo located at ```/home/ubuntu/pythonProjects/UserRepo```
2. Build the Docker image
3. Launch Hugo server in Author Mode

```shell
cd /home/ubuntu/pythonProjects/UserRepo
../docker-run-go build-image author-dev
../docker-run-go launch-server
```
{{% /tab %}}
{{< /tabs >}}
