---
title: "Task 1 - Push content to your repo"
menuTitle: "Git push/Auto-publish"
chapter: false
weight: 2
---

### Push your content to GitHubo repo

- When you're satisfied with the look and feel of your workshop guide locally, **from your local workstation CLI**, push the newly created Hugo site up to GitHub to automatically publish your Hugo Site

   ```shell
     git add .
     git commit -m "<my commit message>"
     git push 
   ``` 

- Remember we're always working in a Git Branch, so you should get in the habit of issuing a Pull request and merge [using our GitFlow procedure](gitflow.html)

  {{% notice info %}} This is mostly applicable when working in a collaborative environment where multiple people may be pushing to the repo with different branches/PR to main.  Strictly speaking, if you're the only person working on this repo and/or it's your first push, this step isn't 100% necessary {{% /notice %}}

  ```shell 
            # locally checkout the main branch
        git checkout main
            # pull the latest version of main from GitHub to your local repo 
        git pull
            # locally checkout your feature branch
        git checkout <branch>
            # locally perform an interactive rebase which locally pull commits from main into my branch
        git rebase main -i 
            # push my local branch (which now includes the latest changes from GH main) up to GitHub remote
        git push --force
  
        ########### WAIT FOR PR APPROVAL
    ```
- Create a PR on GitHub, being sure to select your branch to merge with main. Wait for approval
   
     ![PRScreenshot](GH-PR.jpg)
   - {{% notice info %}} You will not be able to merge the the PR until receiving approval from Jeff or Rob.  They will receive an email for review, but it's a good idea to ping them as a reminder. {{% /notice %}}
     ![PRmergeblock](PR-mergeblocked.jpg)
  - Once your PR is approved, checkout the main branch and perform a fast-forward merge and force push to complete the workflow.
  
      ```shell 
            # locally checkout the main branch
        git checkout main
            # locally merge myFeatureBranch into main with a fast-forward merge scheme
        git merge <feature branch name> --ff-only
            # push local main (which now has myFeatureBranch merged into it) up to GitHub remote  
            # because this push includes the merge it will auto close the PullRequest
        git push
      ```
    
- Once your PR has been approved and your code is in the **_main_** branch, GitHub actions will automatically publish the contents of **/docs** folder to GitHub Pages
  {{% notice tip %}} Remember, Hugo's build wrote the static html pages to the **/public** directory in the container, which is mapped to your **/docs** folder in your local repo{{% /notice %}}

### GitHub Action to Auto Publish
- The file workflows/static.yaml is already included in your repo and triggers a GitHub Action to build and publish your Hugo site every time you push content to GitHub.
- Action:
  - Build a Hugo container with all of our customizations
  - Issue a Hugo Build command to create static HTML site
  - Publish resulting HTML to GitHub Pages for your repo
- You can see action progress and errors in the **Actions** Tab on your repo

