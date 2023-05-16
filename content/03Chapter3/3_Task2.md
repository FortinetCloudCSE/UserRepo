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
- Once your PR has been approved and your code is in the **_main_** branch, GitHub actions will automatically publish the contents of **/docs** folder to GitHub Pages
  {{% notice tip %}} Remember, Hugo's build wrote the static html pages to the **/public** directory in the container, which is mapped to your **/docs** folder in your local repo{{% /notice %}}

