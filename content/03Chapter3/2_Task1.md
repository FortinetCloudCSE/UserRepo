---
title: "Manual Hugo Build"
menuTitle: "Legacy Hugo Build"
chapter: false
weight: 50
---

### Hugo Build

When you're satisfied with Hugo view of your content in Hugo virtual server, issue a Hugo 'build' in the container CLI

```shell
    hugo --minify --cleanDestinationDir
```
        
   - This command "builds" your Hugo site into the container's **_/public_** folder.  We used a docker disk mount to map this folder back to your local **_/docs_** folder, so the Hugo website will automatically be copied back into your local repo
   - flag '--cleanDestinationDir' tells hugo to re-write the entire output directory with its build, so it will clear out template files/anything else that may be in there
   - You can now exit the container with **ctrl + cd**, or command: **'exit'**
   - When you exit the container, any files stored or changes you made to the container will be lost and cannot be recovered
     - **_Remember_** we edited the /content folder on our local OS, so those changes were not made to the container and will not be lost
     - Further, the disk mount from local's **_/docs_** to Container's **_public_** AUTOMATICALLY writes the hugo build to your local OS, so those changes will not be lost
     - If you need to continue editing, just run a new container from your built image, and run hugo's webserver.  Everything is linked properly so it should just work
   