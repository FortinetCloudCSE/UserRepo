---
title: "Upgrade Hugo - container and scripts Update"
linkTitle: "Container Maintenance"
weight: 6
---

## FYI - Upgrading Hugo and the container image

- As a reminder, all the software we're using in this CI/CD process is Open source, and there are active updates to Hugo and the reLearn theme periodically.  As such, we may introduce new features and/or change how we work within this process.

- To simplify the update process and not force you into the sausage making process, we have devised a scheme to update the container and scripts in each repo with minimal manual intervention.
- This process is detailed below.  Follow the tabs in order complete the upgrade (ON AN EXISTING REPO ONLY....this new process is built into any newly created repos)
  - Once you've done this conversion on an existing repo, you should periodically rebuild the container and run it with update_scripts to get any latest features
{{< tabs >}}
{{% tab title="1. Rebuild Old Container" %}}
#### Rebuild Old Container
- Start in the root of your repo directory 
- Rebuild your hugo container with the command below.  
  - This pulls the latest versions if our customized scripts into the existing/"older" container image (running older Hugo version), allowing us to copy some of them back to your repo directory.
```shell
./scripts/docker_build.sh
```
{{% /tab %}}
{{% tab title="2. Update docker_run.sh" %}}  
#### Manually update Docker_run
- Grab a copy of the latest docker run command scripts, located [here](https://raw.githubusercontent.com/FortinetCloudCSE/UserRepo/main/scripts/docker_run.sh)
  - The file is located in the [/scripts directory of our UserRepo in github](https://github.com/FortinetCloudCSE/UserRepo/blob/main/scripts/docker_run.sh)
  - There are countless methods for getting this file, so choose your favorite. (e.g. download from github, wget, copy/paste text)
- Once you have the latest file, overwrite the **docker_run.sh** script in your repo with the latest version
  - **scripts/docker_run.sh**

{{% notice note %}}
This is a chicken and egg problem.  We have everything we need in the refreshed container, but we can't run any of the new features bc our docker_run script is limited to whatever was available when your repo was cloned.

The new run command maps additional local directories to the container allowing us to make updates from the container in the future
{{% /notice %}}
{{% /tab %}}
{{% tab title="3. Update local scripts" %}}
#### Use container script to update the rest of your local scripts
Use the newly updated docker_run.sh script with **update_scripts** option to copy the latest scripts into your local environment/repo directory
```shell
./scripts/docker_run.sh update_scripts
```

This command performs the following:
- From the Container OS/file system, copy the following files into your local environment
  - docker_tester_run.sh --> **scripts/docker_tester_run.sh**
    - update the docker_tester_run script with latest command line options.  The **_tester_** script is used for testing changes to CentralRepo and UserRepo before merging to main
  - docker_run.sh --> **scripts/docker_run.sh**
    - update the docker_run script with latest command line options
  - GitHub Action static.yaml --> **.github/workflows/static.yaml**
    - update GitHub action to reflect latest docker run commands
  - Dockerfile --> **Dockerfile**
    - update Dockerfile to use latest container image and any installed packages
  - IF THERE IS NO **repoConfig.json** file in scripts/
    - repoConfig.json --> **scripts/repoConfig.json**
    - We don't overwrite this file if it's already there :) 
  - Echo 'venv/' to .gitignore
    - ignore Python virtual envs created during generate_toml

{{% notice tip %}}
The most important update is to **Dockerfile**, which now uses a new base container image featuring rolling upgrades to Hugo.  Our old container image was no longer actively supported, so it wasn't getting the latest Hugo updates.

All the rest of of the updates are supporting cast to streamline our scripts, and to simplify future modifications as necessary.
{{% /notice %}}
  
    {{% /tab %}}
    {{% tab title="4. Build New Container" %}}
#### Build New Container
Now that you have the latest Dockerfile (which directs your docker build command to use a new Container image with updated Hugo), we need to re-build the container again:

```shell
./scripts/docker_build.sh
```

The previous container image we were using which included Hugo was no longer maintained, so we had to switch to a new one.  We also install python on the container for use in the next step!

{{% /tab %}}
{{% tab title="5. Generate Hugo.toml file" %}}
#### Generate hugo.toml file
- Due to the nature of Open source software, sometimes there are breaking changes.  In this instance, Hugo is deprecating usage of the config.toml file in favor of a new file named Hugo.toml
- Additionally, as part of the upgrade, we needed to modify some parameters in the file, so we took the opportunity to use a Jinaj2 template to generate the file for with proper parameters
  - This also allows us the ability to update the template in the future and re-generate hugo.toml as necessary
  - Rather than modify Hugo.toml directly, we will now maintain a JSON configuration file **/scripts/repoConfig.json**
- Update `scripts/repoConfig.json` with parameters for your workshop
- Run the container with **generate_toml** option
  - every time you run this command, a new hugo.toml file will be generated
```shell

./scripts/docker_run.sh generate_toml
```

example of repoConfig.toml.  Replace each value with specific parameters for your repo prior to using the generate_toml script:
- repoName (your repo name from GitHub)
- author
- Workshop Title
- themeVariant (options: ["Workshop", "Demo", "UseCase", "Spotlight", "Xperts2024"] )
- logoBannerText (whatever you want in top left Menu under Fortinet Logo.  Leaving this field blank will default to the themeVariant name)
- logoBannerSub Text (optional sub-banner text)
- Shortcuts (Helpful Resources Links in the left menu
  - Text (Display Text)
  - URL (URL for the resource)
  - Icon (from [font awesome free library](https://fontawesome.com/v6/search?o=r&m=free))
  - Weight (low to high ordering of shortcuts)
- DO NOT CHANGE THE FOLLOWING:
  - errorLevel
  - googleServicesID
  
```json
{
  "repoName":"UserRepo",
  "author":"CSE Employee",
  "workshopTitle":"Hugo for Fortinet TECWorkshops",
  "themeVariant":"Xperts-2024",
  "logoBannerText":"",
  "logoBannerSubText":"",
  "errorLevel":"warning",
  "googleServicesID":"G-5RZBH288ST",
  "shortcuts": [
  {
    "text": "Fortinet Cloud CSE GitHub Org",
    "URL": "https://github.com/FortinetCloudCSE",
    "icon": "fa-tools-cap",
    "weight":10
  },
  {
    "text": "Fortinet Standard Workshop Guide",
    "URL": "https://fortinetcloudcse.github.io/UserRepo",
    "icon": "fa-tools-cap",
    "weight":20
  },
  {
    "text": "Fortinet Standard Workshop Template Repo",
    "URL": "https://github.com/FortinetCloudCSE/UserRepo",
    "icon": "fa-tools-cap",
    "weight":30
  },
  {
    "text": "Fortinet Hugo reLearn theme - Guide",
    "URL": "https://mcshelby.github.io/hugo-theme-relearn/index.html",
    "icon": "fa-tools-cap",
    "weight":40
  }
  ]
}
```

{{% /tab %}}
{{% tab title="6. Run Hugo server" %}}
#### Run hugo server
Congratulations!  You've updated everything required to use the latest Hugo version.  Now all you need to do is run the container with server command like normal:

```shell
./scripts/docker_run.sh server
```
{{% /tab %}}
{{< /tabs >}}

### Container Flow Visual

{{< ContainerFlow >}}