---
title: "Task 4 - image storage"
menuTitle: "d: images"
chapter: false
weight: 4
---

### Task 4: Image Storage

- Option 1: use externally fully qualified absolutely path (this can be a pain)
- Option 2: if you have a directory with all your images.... 
  - put it in "/content/images"
  - MD usage(from a chapter page in "content/chapter01"): ![Magic](../images/magic.gif)
- Option 3:  I find it easier to organize images with the pages they go with (this is how the template repo is setup
  - put images in the chapter directory
        1	e.g. images in "/content/chapter1/"
        2	MD Usage ![Magic](magic.git)
  (venv) jkopko@jkopko-mac content % tree
.
├── 01GettingStarted
│   ├── 2_Task1.md
│   ├── ContainerBuild.md
│   ├── ContainerRun.md
│   ├── LocalHugoInstall.md
│   ├── _index.md
│   └── hugoServer.jpg
├── 02Chapter2
│   ├── 2_Task1.md
│   ├── 3_Task2.md
│   ├── 4_Task3.md
│   ├── _index.md
│   ├── chapterIndex.png
│   ├── config.png
│   ├── images.md
│   └── taskPage.png
├── 03Chapter3
│   ├── 2_Task1.md
│   ├── 3_Task2.md
│   ├── GitHubActions.md
│   ├── Gittips.md
│   ├── _index.md
│   ├── actionsReview.png
│   ├── hugoCommit.png
│   ├── hugoCommitNewFile.png
│   ├── img.png
│   ├── pages-browseWorkflows.png
│   ├── pages-deployAction.png
│   ├── pages-workflowHugo.png
│   ├── repoFolders.png
│   ├── repoPages.png
│   └── repoSettings.png
└── _index.md
