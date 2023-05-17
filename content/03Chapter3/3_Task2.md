---
title: "Task 2 - Push content to your repo"
menuTitle: "Git push"
chapter: false
weight: 2
---

### Push your content to GitHubo repo

- Finally, **from your local workstation CLI**, push the newly created Hugo site up to GitHub to automatically publish your Hugo Site

   ```shell
   git add .
   git commit -m "<my commit message>"
   git push 
   ``` 

- Remember we're always working in a Git Branch, so we'll need to issue a Pull request and merge [using this procedure](gittips.html)

  ```shell 
            # locally checkout the main branch
        git checkout main
            # pull the latest version of main from GitHub to your local repo 
        git pull
            # locally checkout your feature branch
        git checkout <branch>
            # locally pull commits from main into my branch with a fast-forward merge scheme
        git merge main --ff-only
            # locally perform an interactive rebase
        git rebase -i 
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

