---
title: "Background Procedures - CentralRepo Maintenance"
linkTitle: "FYI - Central Repo"
weight: 20
---

## CentralRepo

[CentralRepo](https://github.com/FortinetCloudCSE/CentralRepo) contains all of the stuff Hugo needs to build a static website, including Fortinet Customizations to themes.


### How it's used

- Generally TEC Program participants creating content for Workshops, Demos, User Cases, or Spotlights don't need to worry about Central Repo at all
- When you build your container, it inherently grabs the latest copy of CentralRepo:main from github, via this command in Dockerfile:
  ```shell
    ADD https://github.com/FortinetCloudCSE/CentralRepo.git#main /home/CentralRepo
  ```
- This means that you can re-use the same container for every TEC workshop guide you create.
{{% notice tip %}} If you haven't used your container in a while, it's a good idea to rebuild it so it will grab the latest version of CentralRepo {{% /notice %}}

### Repo Maintenance

- CentralRepo is maintained by the [Fortinet Cloud CSE team](mailto:fortinetcloudcse@fortinet.com), so work with us to make any changes necessary.
- Review, modification, and testing process:
  - Anyone can fork CentralRepo and modify as necessary.
  - Once you've tested your modifications, submit a PR to Central Repo
  - [Fortinet Cloud CSE team](mailto:fortinetcloudcse@fortinet.com) will merge your PR changes into branch [CentralRepo:prreviewJune23](https://github.com/FortinetCloudCSE/CentralRepo/tree/prreviewJune23)
  - Test using HugoDevContainer pointing to the **merged branch** rather than **main**
  ```shell
      ./scripts/docker_tester_build.sh
      ./scripts/docker_tester_run.sh

  ```
  {{% notice warning %}} **IMPORTANT** If there is collaborative work while testing a PR, be sure to always pull latest from the PR Branch before starting new work!
  ```shell
       git checkout PRBranch
       git remote add <PR Label> git@github.com:FortinetCloudCSE/CentralRepo.git
       git pull prreviewJune23
  ```
  {{% /notice %}}

  - Upon successful testing, Fortinet Cloud CSE team will merge the branch to main and close PR 
  ```shell
      git checkout prreviewJune23
      git remote add <PR label> <remote Github ssh URL>
      git pull <PR label>
      
      <PERFORM TESTIGN ON CONTAINER, and make any changes as necessary on this branch>
    
      <UPON SUCCESSFUL TESTING>
      git checkout main
      git merge prreviewJune23 --ff-only
      git push 
  
      <Manually Close PR>
      
  ```