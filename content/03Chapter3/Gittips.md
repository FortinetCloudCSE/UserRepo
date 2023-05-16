---
title: "Git command Line Tips"
menuTitle: "Git Tips"
chapter: false
weight: 5
---

## GitHub Repo Getting Started (General Workflow for GitHub Repos)

1.  Once your repo and pipeline have been created, you will be provided with the GitHub repo link which you can use to clone and begin content creation. First, navigate to a desired local directory and clone the repo with the provided link:

  ```shell
    cd <desired parent directory>
    git clone <provided link>
    cd <cloned repo directory>
  ```
2. Create a feature branch to begin working on your desired changes.

  ```shell
  git checkout -b <FEATURE-username-ShortDescr>
  ```

3. Check the repo status to verify the changes to be staged.

  ```shell
  git status
  ```

4. Stage the desired files (or issue -A (or .) for all), commit, and push.

  ```shell
  git add -A {or} git add .
  git commit -m "<add a commit message here>"
  git push
  ```
  If this is your first push to the branch, GitHub upstream doesn't know about it.  Just go ahead and use the provided command in this case to perform the push, which will create the upstream branch
  - To auto create new branches when you first push, update Git global config 

  ```shell
  git config --global --add --bool push.autoSetupRemote true
  ```


  Tip: An easy way to squash your commits is to perform a soft reset:
  ```shell
  git reset --soft <hash of the last commit you want to keep as is>
  git add -A
  git commit -m "<new commit message>"
  git log
  ```
  You will see the new commit on top of the one you referenced in the git reset command.

5. When you have completed your work and are ready to merge your changes into the main branch, ensure your branch is up to date with the main branch.

  ```
  git checkout main
  git pull
  ``` 

  Then, you can perform an interactive rebase and force push to your branch.

  ```shell
  git rebase -i
  ```
  On the first screen, you may want to leave the top commit as is, and for the rest, replace the word 'pick' with an 's' for squash. Then, on the next screen, comment out the commit messages you don't want, leaving the preferred one as is. Once your PR is approved, checkout the main branch and perform a fast-forward merge and force push to complete the workflow.
  
  ```shell 
  git checkout main
  git merge <feature branch name> --ff-only
  git push --force
  ```
