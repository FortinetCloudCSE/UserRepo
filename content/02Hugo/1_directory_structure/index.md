---
title: "Task 1 - Chapter Directory Structure"
linkTitle: "Directories"
weight: 10
---

### Create a Folder structure correlating to the major topics/sections of the demonstration

1. Browse to the **content** directory within your TECWorkshop repo (Locally on your machine)
  * The Left Hand navigation menu is driven by the folder structure you create
  * Folder naming drives site navigation, content hierarchy, and helps organize the overall site layout.  Specifically, directory naming helps to identify what's in each Chapter & task

2. Within each folder there is an **_index.md** file (For Chapter/Section pages) or **index.md** (for regular/leaf pages) which will be used to hold content for that Chapter/Directory/Task
  * The metadata header on that page is used to set
    1. Title of the Page 
    2. Link Title (as it appears in the leftNav bar)
    3. Weight the order of chapters or tasks in the leftNav bar
  * Notice the folder structure and file naming on the left and the resulting display on the right
  {{% notice info %}} Note that the file and folder names only matter for ordering in your directory listing in your IDE.  Lower numbered folders will appear first, but it's really the _index.md weight metadata field which influences the chapter or task ordering.  Only the "title" tag within each Markdown file will impact the resulting page view {{% /notice %}}

  | image reference # | Folder/File Name | Page Type  | Weight 
  |---|------------------|----------------------|--------|
  | 1 | content/01GettingStarted/_index.html |  Chapter Heading Page| 8 (Global Chapters)|
  | 2 | content/02Hugo/1_directory_structure/index.html | task page (Hugo Page Bundle) | 10 (within Chapter 02) |


   {{< figure src="newdirectorystructure.png" alt="chapterIndex" class="zoomable" >}}
  

3. Subsequent Markdown pages under each folder are used to explain tasks/steps within each chapter
  
  ```bash
  ubuntu@ip-172-31-20-10:~/pythonProjects/UserRepo$ tree
.
├── README.md
├── content
│   ├── 00ChangeLog
│   │   └── _index.md
│   ├── 01GettingStarted
│   │   ├── 1_UserRepo
│   │   │   ├── forticloud-iam-login.png
│   │   │   └── index.md
│   │   ├── 2_HugoFrontmatter
│   │   │   └── index.md
│   │   ├── 3_FortiHugoRunner
│   │   │   ├── docker-base-image.png
│   │   │   └── index.md
│   │   ├── 4_Docker-helpful-hints
│   │   │   └── index.md
│   │   ├── 5_CLITroubleshooting
│   │   │   ├── index.md
│   │   │   ├── mac-go-binary-issue.png
│   │   ├── 6_CentralRepo
│   │   │   └── index.md
│   │   ├── _index.md
│   ├── 02Hugo
│   │   ├── 1_directory_structure
│   │   │   ├── chapterIndex.png
│   │   │   └── index.md
│   │   ├── 2_page_bundles
│   │   │   └── _index.md
│   │   ├── 3_create_md
│   │   │   ├── index.md
│   │   │   └── taskPage.png
│   │   ├── 4_images
│   │   │   └── index.md
│   │   ├── 5_shortcodes
│   │   │   └── index.md
│   │   ├── _index.md
│   │   └── config.png
│   ├── 03Chapter3
│   │   ├── 1_push_publish
│   │   │   └── index.md
│   │   ├── 2_gitflow
│   │   │   └── index.md
│   │   ├── 3_legacy
│   │   │   └── index.md
│   │   ├── _index.md
│   ├── _index.md
├── layouts
│   └── shortcodes
│       ├── someshortcode.html
└── scripts
    └── repoConfig.json
```