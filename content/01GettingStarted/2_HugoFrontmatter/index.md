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
- {{% badge style="note" title=" " color="magenta"%}}TLDR{{% /badge %}} Update `scripts/repoConfig.json` with parameters for your workshop
- Every time the container runs it first executes a script  **generate_toml** which will generate the hugo.toml file
  - {{% badge style="info" color="orange" icon="fa-fw fas fa-exclamation-triangle" title=" " %}}Change{{% /badge %}} you will no longer see config.toml or hugo.toml in your repo!  It's created automatically for you, and only exists while the container is running.

example of repoConfig.json.  Replace each value with specific parameters for your repo:
- repoName (your repo name from GitHub)
- author
- Workshop Title
- themeVariant (options: ["Workshop", "Demo", "UseCase", "Spotlight", "Xperts2024", "Xperts2025", "CloudCSEMovie"] )
- logoBannerText (whatever you want in top left Menu under Fortinet Logo.  Leaving this field blank will default to the themeVariant name)
- logoBannerSub Text (optional sub-banner text)
- marketingCode (optional marketing code to be used as default in analytics gathering and provisioning form)
- bannerLine1 (optional text for XPerts Content Header banner line 1)
- bannerLine2 (optional text for XPerts Content Header banner line 2)
- bannerLine3 (optional text for XPerts Content Header banner line 3)
- quizUrl (optional URL for quiz to be used in the quiz shortcode)
- videoHeaderSrc (optional, **CloudCSEMovie theme only** — URL path to the MP4, e.g. `"/videos/header-bg.mp4"`. Hugo strips the `static/` prefix — do NOT include it in the path. Leave blank to disable.)
- videoHeaderInterval (optional, **CloudCSEMovie theme only** — total seconds between the start of each video play cycle. Defaults to `60`. Must be greater than the video duration.)
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
  "themeVariant":"CloudCSEMovie",
  "logoBannerText":"",
  "logoBannerSubText":"",
  "errorLevel":"warning",
  "googleServicesID":"G-5RZBH288ST",
  "marketingCode": "MGO12345",
  "bannerLine1":"Workshop Type ID Eg: Public Cloud 101",
  "bannerLine2":"Workshop Title Here",
  "bannerLine3":"Subtitle,Description, or 3rd line Here",
  "quizUrl": "https://forms.gle/yourformhere",
  "videoHeaderSrc": "/videos/header-bg.mp4",
  "videoHeaderInterval": "60",
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

---

## CloudCSEMovie Theme — Video Header Background

The `CloudCSEMovie` theme variant replaces the static header image with a looping MP4 video in the sidebar header area (the same region used by the Xperts background image).

### How it works

- The video plays automatically on page load (muted, no controls)
- When the video ends, it pauses and replays after a configurable interval — for example, a 6-second video with a 60-second interval plays once, waits 54 seconds, then plays again
- All other header content (logo, banner text, search bar) renders on top of the video

### Setup steps

**1. Add your MP4 to the repo**

Place the video file in your repo's `static/videos/` folder:

```
static/
  videos/
    header-bg.mp4
```

**2. Configure repoConfig.json**

```json
{
  "themeVariant": "CloudCSEMovie",
  "videoHeaderSrc": "/videos/header-bg.mp4",
  "videoHeaderInterval": 60
}
```

- `videoHeaderSrc` — the URL path to your MP4, relative to the site root. Required for the video to appear.
- `videoHeaderInterval` — total seconds from the start of one play to the start of the next. Optional; defaults to `60`. Set this to a value greater than your video's duration.

{{% badge style="note" title=" " color="magenta"%}}Tip{{% /badge %}} Leave `videoHeaderSrc` as an empty string `""` to use the `CloudCSEMovie` theme without a video (renders a solid color header like other themes).

{{% badge style="info" color="orange" icon="fa-fw fas fa-exclamation-triangle" title=" " %}}Note{{% /badge %}} The MP4 file is committed to your repo inside `static/videos/`. Keep it small — short clips under 5MB are ideal for fast page loads.