---
title: "Task 3 - Run Container"
menuTitle: "c: Run Container"
weight: 5
---

## Task 3: Run FortinetHugo container 

{{% notice info %}} If you used the scripts to build and run container from last step, your container is already running {{% /notice %}} 

- Run the container with local disk mounts so you review your markdown TECWorkshop Guide as you're creating the content (repeat this procedure for any TECWorkshop you're creating) 

    ```shell
    docker run --rm -it -v $(pwd)/content/:/home/CentralRepo/content -v $(pwd)/config.toml:/home/CentralRepo/config.toml -v $(pwd)/docs:/home/CentralRepo/public  -p 1313:1313 fortinet-hugo:latest
    ```
   - '-rm' flag removes the container after it's closed...freeing up resources
   - '-it' flag provides an interactive prompt into the Container
   - '-v' flag creates a disk mount to the local file system available within the container OS
   - '-p' publishes container ports to the local OS (used to view the local Hugo Webserver)
    
- the above command runs the container and logs you into the container Ubuntu OS CLI (most Linux commands will work)
  - Refresh any updates from CentralRepo, note the $(pwd) in Container OS, and list files, 
  
    ```shell
    git pull -r
    pwd
    ls -la 
    ```
    {{% notice info %}} If your hugo website doesn't have the Fortinet logo or the proper colors, it's likely b/c you haven't refreshed the CentralRepo content with 
      ``` git pull -r ```
    {{% /notice %}}

- Run Hugo virtual server to get a live view of Hugo's output 

  ```
  hugo server --bind 0.0.0.0
  ```
  In your local machine, browse to http://localhost:1313/UserRepo
