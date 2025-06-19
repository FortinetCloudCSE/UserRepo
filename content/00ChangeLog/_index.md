---
title: "What's New"
linkTitle: "What's New"
weight: 5
---

### This is a list of new features and/or changes in a given version

---

## 2025

### May - **MVP 2.1** **_CURRENT VERSION_**

- {{% badge style="info" color="orange" icon="fa-fw fas fa-exclamation-triangle" title=" " %}}Change{{% /badge %}} [Go Utility](../xx-GettingStarted-old/FortiHugoRunner.html) will be the primary mechanism to work with our process going forward.  It will continue to get iterative feature enhancements, so please update it often!
- {{% badge style="note" title=" " color="magenta"%}}Update{{% /badge %}} Hugo relearn theme update due to bug in compatability this Hugo versions 146 and later
- {{% badge style="info" color="orange" icon="fa-fw fas fa-exclamation-triangle" title=" " %}}Change{{% /badge %}} Generate_toml runs on any container restart, so you never have to run it yourself and it will always update whenever you make changes
 
### March - MVP 2.0

- {{% badge style="info" color="orange" icon="fa-fw fas fa-exclamation-triangle" title=" " %}}Change{{% /badge %}} Require Checkin at each repo front page before browsing any further content.
  - Checkin data is used by [Analytics gathering](https://tecanalytics.forticloudcse.com/) and issues a cookie valid for 5 days across our workshop estate.  Collecting:
    - e-mail address
    - SMART Ticket
    - Marketing Code
  - {{% badge style="info" icon="fa-solid fa-circle-plus" title=" " %}}New{{% /badge %}} De-coupled [analytics check-in](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/layouts/partials/analytics_checkin.html) functionality from [Lab provisioning shortcode](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/layouts/shortcodes/launchdemoform.html).  
    - Check-in is automatically included on every repo.
    - Lab provisioning shortcodes should be included on labs featuring Azure automated provisioning scripts, and **REMOVED** from workshops which don't require Azure provisioning.
  - Added [Author mode](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/scripts/hugoServer_authorMode.sh) so analytics check-in **NOT REQUIRED** while locally authoring workshops.
- {{% badge style="info" color="orange" icon="fa-fw fas fa-exclamation-triangle" title=" " %}}Change{{% /badge %}} Introduced [Go Utility](../xx-GettingStarted-old/FortiHugoRunner.html) to simplify workshop authoring from different systems
  - When this Utility and documentation is polished, it will eliminate the need for docker_build/_run scripts in each repo and the tax of maintaining/updating them.
- {{% badge style="info" icon="fa-solid fa-circle-plus" title=" " %}}New{{% /badge %}} Created [utility](https://github.com/FortinetCloudCSE/CentralRepo/blob/prreviewJune23/scripts/upgrade_repo.sh) to upgrade older repos to latest feature set including automated conversion of config.toml to repoConfig.json/hugo.toml 
- {{% badge style="note" title=" " color="magenta"%}}Update{{% /badge %}} Update [gitHub action](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/scripts/static.yml) to use latest API versioned commands 
- {{% badge style="info" icon="fa-solid fa-circle-plus" title=" "%}}New{{% /badge %}} Added [Quizdown shortcode](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/layouts/shortcodes/quizdown.html). Check [MD Page](../02Hugo/3_Task2.html) for usage instructions 
---

## 2024

### Oct - MVP 1.2

  - {{% badge style="info" color="orange" icon="fa-fw fas fa-exclamation-triangle" title=" " %}}Change{{% /badge %}} Switched to new container base image from [hugomods](https://docker.hugomods.com/docs/introduction/)
    - continuous support for latest Hugo version releases
    - Upgraded ReLearn theme to 6.0.0
      - added features for [tabbed content](https://mcshelby.github.io/hugo-theme-relearn/shortcodes/tab/index.html)
  - {{% badge style="info" color="orange" icon="fa-fw fas fa-exclamation-triangle" title=" " %}}Change{{% /badge %}} Created a simplified/scripted procedure to convert workshop repos using older containers to the latest:
    - Container based scripting to [update local scripts](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/scripts/update_scripts.sh)
    - Add python and Jinja2 to container to facilitate [templetized creation of site frontmatter (hugo.toml)](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/scripts/generate_toml.py)
    - Revise [container run scripts](https://github.com/FortinetCloudCSE/CentralRepo/blob/main/scripts/docker_run.sh) to allow new options and future updates 
  - {{% badge style="note" title=" " color="magenta"%}}Update{{% /badge %}}  Theme updates
    - author customizable banners for Xperts2024
    - [copyright info on home page](../)
    - modify code highlighting color scheme to improve readability
  - {{% badge style="info" icon="fa-solid fa-circle-plus" title=" "%}}New{{% /badge %}}Analytics
    - Add analytics capabilities to track site activity across entire Cloud TEC workshop catalog.
    
---
## 2023

### June - MVP 1.1

  - reduce container size (using Alpine to get shell.  BusyBox does not have shell)
  - autopublish action on GitHub (run our container as GitHub action to perform Hugo build w/ CentralRepo)
    - eliminates need to store Hugo static HTML (autopublish action directly publishes to GH pages)
  - Move Shortcodes from CentralRepo to UserRepo
  - Add CentralRepo/scripts/local_copy.sh to copy any local shortcodes or partials into container
  - Modify logo.html to read Params for logoBanner & logoBannerColor
  - Standardize themes and colors for Workshop, UseCase, Spotlight, Demo
  - Modify Banner Text and Subtext to match theme and be customizable 
  - Add ability to run container run in "build", "server", or "shell" mode
  - Added Dev container env & workflow to stage and test changes before promoting to main/Prod


### May - MVP 1.0
  - Separated UserRepo and Central Repo to allow maximum re-usability & future-proofing for style/format changes
    - Standard Repo has Fortinet reLearn theme Variant & all necessary customizations
  - Swap in Hugo ReLearn theme (actively community supported) and eliminate Learn & Notice themes (inactive development)
  - Ubuntu container:
    - Maintain consistent Hugo version and eliminate need for local installs
    - allow continuous improvement to our process via container improvements without adding burden to CSE Team
  - Use Container for Hugo Build & GitHub action to publish/refresh GitHub Pages
  - Containerizing our development efforts allows for a lightweight development area while eliminating redundant componentry every time we create a new repo/workshop/demo, and allowing simple and automated updates to existing workshops when the parent template changes.
       - Ultimately we'd like to have scripting copy/revise parent templates periodically and/or whenever we create new Workshops  
  - First TECWorkshop re-published with this new workflow: https://fortinetcloudcse.github.io/FortiCNF/
### March - MVP 0.2
  - created FortiCloudCSE GitHub Org
  - begin separation of UserRepo & Central Repo
  - begin investigation into container workflow

### Jan - MVP 0.1
  - Single repo, manual copy of theme, no use of submodules
  - Introduce Hugo, Learn theme & first draft at Learn theme Variant
  - Use GitHub action to build and Publish to Pages
  - First TECWorkshop published: https://fortinetsecdevops.github.io/technical-recipe-azure-sdwan/