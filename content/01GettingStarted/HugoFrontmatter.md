---
title: "Hugo Frontmatter"
linkTitle: "Hugo Frontmatter"
weight: 9
---

## First step on every new repo!


- Due to the nature of Open source software, sometimes there are breaking changes.  In this instance, Hugo has deprecated usage of the config.toml file in favor of a new file named Hugo.toml
- Additionally, as part of the upgrade, we needed to modify some parameters in the file, so we took the opportunity to use a Jinaj2 template to generate the file for with proper parameters
  - This also allows us the ability to update the template in the future and re-generate hugo.toml as necessary
  - Rather than modify Hugo.toml directly, we will now maintain a JSON configuration file **/scripts/repoConfig.json**
- Update `scripts/repoConfig.json` with parameters for your workshop
- Every time the container runs it first executes a script  **generate_toml** which will generate the hugo.toml file
  - you will no longer see config.toml or hugo.toml in your repo!

example of repoConfig.toml.  Replace each value with specific parameters for your repo prior to using the generate_toml script:
- repoName (your repo name from GitHub)
- author
- Workshop Title
- themeVariant (options: ["Workshop", "Demo", "UseCase", "Spotlight", "Xperts2024"] )
- logoBannerText (whatever you want in top left Menu under Fortinet Logo.  Leaving this field blank will default to the themeVariant name)
- logoBannerSub Text (optional sub-banner text)
- marketingCode (optional marketing code to be used as default in analytics gathering and provisioning form)
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
  "marketingCode": "MGO12345",
  "shortcuts": [
  {
    "text": "Fortinet Cloud CSE GitHub Org",
    "URL": "https://github.com/FortinetCloudCSE",
    "icon": "fa-graduation-cap",
    "weight":10
  },
  {
    "text": "Fortinet Standard Workshop Guide",
    "URL": "https://fortinetcloudcse.github.io/UserRepo",
    "icon": "fa-tools",
    "weight":20
  },
  {
    "text": "Fortinet Standard Workshop Template Repo",
    "URL": "https://github.com/FortinetCloudCSE/UserRepo",
    "icon": "fa-tools",
    "weight":30
  },
  {
    "text": "Fortinet Hugo reLearn theme - Guide",
    "URL": "https://mcshelby.github.io/hugo-theme-relearn/index.html",
    "icon": "fa-tools",
    "weight":40
  }
  ]
}
```