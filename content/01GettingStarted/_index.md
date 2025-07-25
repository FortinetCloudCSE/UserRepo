---
title: "Ch 1 Getting Started with Repos, Containers, and Hugo"
linkTitle: "Ch 1: Setup - NEW"
weight: 8
#archetype: "chapter"
---
{{% badge style="info" color="orange" icon="fa-fw fas fa-exclamation-triangle" title=" " %}}Change{{% /badge %}}
{{% badge style="info" icon="fa-solid fa-circle-plus" title=" " %}}New{{% /badge %}}

### ***Setting up your Hugo environment (15 min)***
---
## Prereqs
  - Docker - older installs won't work, so if you need to upgrade/reinstall
    - You can use your docker flavor of choice.  Keep in mind Docker Desktop is no  longer free for enterprise use.
    - We've tested [Rancher Desktop](https://rancherdesktop.io/), which works well.  Caveat...your locally rendered version of the site may not update in real time as you modify content, so you may need to restart the server to see new content
  - GitHub keys (to clone GitHub repos using SSH which will eliminate Headaches later down the line with Authentication)
    - Follow the instructions [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) to generate a new SSH key pair
       {{% notice warning %}} DO NOT USE A PASSPHRASE when you create the keys {{% /notice %}}
    - Once created follow [these directions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) to add the newly created Key to your GitHub account.

### What is Hugo and how easy can this be?

- The site you are viewing right now is built with Hugo.
- You can navigate to specific chapters and tasks with the Left Navbar or the top banner table of contents
  - For a sequential step by step flow through this workshop, use the arrows in the upper right corner to go through each step individually

### Development Environment Options

- To start, you'll [request a new repo which is a clone of User Repo](01gettingstarted/userrepo.html).
  - you'll create the content for your TECWorkshop guides in this repo, and ultimately publish the Hugo built website to GitHub Pages
- Once you have UserRepo, you can choose how to use Hugo 

1. {{% badge style="info" icon="fa-solid fa-circle-plus" title=" " %}}New{{% /badge %}}[Option 1](01gettingstarted/FortiHugoRunner.html) **RECOMMENDED METHOD**: Use the Go Utility flavored for your OS/Architecture to build and run our container seamlessly.
2. [Option 2](01gettingstarted/containerbuild.html): build a container with Hugo installed on it and a copy of all Fortinet specific customizations to the Hugo reLearn theme 
   - Beyond providing an opportunity to learn the basics of container development, this option:
      - streamlines and simplifies the Hugo content creation process
      - minimizes local storage/upkeep of reusable componentry
      - reduces complications of version dependencies in development environment for Hugo or the reLearn theme
      - future-proofs the content created for any given TECWorkshop so that any Fortinet branding changes can be easily re-applied to all guides
2. [Option 3](01gettingstarted/localhugoinstall.html): **THIS OPTION IS INCLUDED FOR POSTERITY ONLY** Install Hugo locally on your laptop/workstation and clone CentralRepo
   - You'll have to 
     - maintain CentralRepo including submodules on your local workstation
     - ensure your final site is published to the /docs folder in your UserRepo

