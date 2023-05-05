---
title: "Task 1 - Clone sample repo"
menuTitle: "a: Clone"
weight: 1
---

# MVP1 - in progress 

## Task 1 - Create Repo

1. Use the Jenkins Script with GH credentials to create a new repo in the FortinetCloudCSE GitHub account
- For now this is limited to Jeff & Rob
```shell
  ./setup-gh-jenkins <Your Jenkins user id> <Name of Repo Template> <Name of New Repo to be created> <Github username of user to be added as collaborator> [-p]
```

This script will:
1. Create a new repo in FortinetCloudCSE from the Parent Template DemoFrontEndDocker
2. Add specified GitHub collaborators to the newly created Repo
3. Create a Jenkins job for the repo and  run initial build.  This job can/will do things like
   1. linting
   2. Directory governance
   3. FortiDevSec scans

---

# MVP0 (LEGACY STEPS only do this if MVP1 steps don't work) 

### Task 1 - Clone this sample repo

__** Prerequisite **__ - Ensure Git is installted on your system

## Step 1 Clone this [git repo](https://github.com/FortinetCloudCSE/DemoFrontEndDocker.git) 

```shell
git clone https://github.com/FortinetCloudCSE/DemoFrontEndDocker.git --recurse-submodules
```

