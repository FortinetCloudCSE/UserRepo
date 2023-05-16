---
title: "Ch 2 Hugo Content Structure"
chapter: false
menuTitle: "Ch 2: Hugo Content"
weight: 20
---

### ***Learn to organize and create content in Hugo- estimated duration 20min***

You now have a container running hugo webserver and tracking changes to the **_/content_** directory in your repo.  

  - Create your TecWorkshop Guide including Chapers and tasks.  You can use your favorite editor/IDE to create the markdown pages
  - Depending on several factors, you may or may not see LIVE changes to the [http://localhost:1313/UserRepo](http://localhost:1313/UserRepo) page  
    - If you're not seeing live changes... re-run hugo server command on container (ctrl+C to end the running hugo process on container CLI)

{{% notice note %}}  You will ultimately need to make a minor change to the **_config.toml_** file in this repo, and when you do, the Hugo Local Webserver directory will change to the name of your repo {{% /notice %}}


With your FortinetHugo Container running, you can proceed to creating and editing your demonstration content.

Hugo is incredibly powerful and allows many customizations, and we won't cover most of theme here as they've already been set for Fortinet's standard template  

Generally, you only need to do 3 things:
1. Set the folder structure for left hand menu bar navigation/topic structure, according to your chapters and tasks
2. Create Markdown files for each Chapter and and discrete Task task therein
3. Adjust the site's frontmatter settings via config.toml to reflect your TECWorkshop repo name

Click the right arrow to go through each step individually
