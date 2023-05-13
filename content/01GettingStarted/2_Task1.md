---
title: "Task 1 - Repo Creation"
menuTitle: "a: Repo"
weight: 1
---

## Task 1 - Create Repo - 

Request a new repo for your TECWorkshop (this will be referred to as your **_UserRepo_**)
   - Send an email to [fortinetcloudcse@fortinet.com](mailto:fortinetcloudcse@fortinet.com) to request a new GitHub repo and Jenkins Pipeline. Providing the following:
     - Repo Name <Fortinet-Product-CSP-Feature>
     - GitHub Usernames of collaborators
   - Behind the scenes, a script is used to create your TECWorkshop repo with appropriate protections and features.  Additionally a Jenkins pipeline will be setup to monitor changes to the repo and run things like 
     - publishing the web site
     - FortiDevSec scanning
  - You will use this repo to create and modify MD chapters & tasks to create your workshop Guide in Hugo format
    - Help with Git is included below

This script will:
1. Create a new repo in FortinetCloudCSE from the Parent Template DemoFrontEndDocker
2. Add specified GitHub collaborators to the newly created Repo
3. Create a Jenkins job for the repo and  run initial build.  This job can/will do things like
   1. linting
   2. Directory governance
   3. FortiDevSec scans

## Git repo setup

- Once your TECWorkshop repo is created, clone the repo and change your working directory to the cloned repo

```shell
    git clone <provided link>
    cd <cloned repo directory>
```

- additional [Git Tips are available here](../03chapter3/gittips.html)
### MVP0 (LEGACY STEPS only do this if MVP1 steps don't work) 

{{% notice info %}} You won't be able to clone this repo into the FortinetCloudCSE Org, so using this route, you'll have to clone to your own repo {{% /notice %}}  

### Task 1 - Clone this sample repo

__** Prerequisite **__ - Ensure Git is installted on your system

## Step 1 Clone this [git repo](https://github.com/FortinetCloudCSE/UserRepo.git) 

```shell
git clone https://github.com/FortinetCloudCSE/UserRepo.git
```

