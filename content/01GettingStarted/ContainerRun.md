---
title: "Task 3 - Run Container"
menuTitle: "Run Container"
weight: 5
---

## Task 3: Run FortinetHugo container 

- Run the container with local disk mounts so you review your markdown TECWorkshop Guide as you're creating the content (repeat this procedure for any TECWorkshop you're creating) 
    {{% notice tip %}} The Full commands and explanation for running your pre-build docker are listed below.  We've also included a shell script in this repo to run your container image 
    ```
        ./scripts/docker_run.sh
    ```
    {{% /notice  %}}

    ```shell
      docker run --rm -it -v $(pwd)/content/:/home/CentralRepo/content -v $(pwd)/config.toml:/home/CentralRepo/config.toml -v $(pwd)/docs:/home/CentralRepo/public  -p 1313:1313 fortinet-hugo:latest
    ```
     - '-rm' flag removes the container after it's closed...freeing up resources
     - '-it' flag provides an interactive prompt into the Container
     - '-v' flag creates a disk mount to the local file system available within the container OS
     - '-p' publishes container ports to the local OS (used to view the local Hugo Webserver)
      
- the above command runs the container and logs you into the container Ubuntu OS CLI (most Linux commands will work)
  - Note the $(pwd) in Container OS, and list files.  You'll see you have everything needed to create your Hugo site! 
  
    ```shell
    pwd
    ls -la 
    ```

- Run Hugo virtual server to get a live view of Hugo's output 

  ```
  hugo server --bind 0.0.0.0
  ```
  In your local machine, browse to http://localhost:1313/UserRepo

  You'll see a template hugo site served by Hugo's local webserver.  Now you're ready to proceed building your [TECWorkshop content](../02hugo.html) in the next chapter!

- To exit out of the Container OS: use 'exit' or **CTRL+d**

  ```shell
  exit
  ```

---

{{% notice tip %}} We're including some helpful docker commands here for reference.  Use these if you've built LOTS of images and you need to get rid of the mess
{{% /notice  %}}



### Notes:
- Inside the container, [Central Repo](https://github.com/FortinetCloudCSE/CentralRepo) (which is where we'll make any template changes) is cloned and integrated with your repo.
- Container (ideally) displays local version of Hugo site updating near real time as you create content
- To run a container interactively (for troubleshooting or to see how they function)
  - Comment out any offending lines in the dockerfile
  - Build again using commands above.
  - to run the container interactively use the '-it' flag:

  ```shell
    docker run --rm -it fortinet-hugo:latest
  ```

- Container outputs /public folder which is the result from "Hugo build"
  - This /public(/docs) folder can be hosted anywhere.  We'll still use GH Pages to host the actual page.

### Useful Docker Commands to Know
```
docker images                                           #List all images
docker ps -a                                            #List all containers, both running and stopped
docker rmi <image-id>                                   #Remove an image
docker rmi $(docker images -aq)                         #Remove all images
docker rmi $(docker images -filter dangling=true -aq)   #Remove all images with tag <none>
docker rm <container-id>                                #Remove a container
docker rm $(docker ps -aq)                              #Remove all containers
docker builder prune                                    #Remove build cache
```
When running any of the above commands, if you get an error message indicating an image or container is being used or referenced in another image or container, you can issue the '-f' flag to force remove.

