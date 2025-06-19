---
title: "Ch 2 Hugo Content Structure"
chapter: false
linkTitle: "Ch 2: Hugo Content"
weight: 20
---

### ***Learn to organize and create content in Hugo- estimated duration 20min***

You now have a container running hugo webserver and tracking changes to the **_/content_** directory in your repo.  

  - Create your TecWorkshop Guide including Chapters and tasks.  You can use your favorite editor/IDE to create the markdown pages
  - As you make changes to the MD files, you'll see LIVE changes to the your local copy of the workshop guide (which depending on your ENV setup may or may not be viewable at: [http://localhost:1313/<your_repo_name>](http://localhost:1313/<your_repo_name>)

With your FortinetHugo Container running, you can proceed to creating and editing your workshop content.

Hugo is incredibly powerful and allows many customizations, and we won't cover most of theme here as they've already been set for Fortinet's standard template  

Generally, you only need to do 3 things:
1. Set the folder structure for left hand menu bar navigation/topic structure, according to your chapters and tasks
2. Create Markdown files for each Chapter and discrete task therein
3. Adjust the site's frontmatter settings via your_repo_name/scripts/repoConfig.json to reflect your TECWorkshop repo name, metadata, and leftnav URLs

Click the right arrow to go through each step individually
