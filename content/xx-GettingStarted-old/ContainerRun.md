---
title: "Task 3 - Run Container"
linkTitle: "Run Container"
weight: 5
---

## Task 3: Run FortinetHugo container 

- Run the container with local disk mounts so you can review your markdown TECWorkshop Guide as you're creating the content (repeat this procedure for any TECWorkshop you're creating)

{{% notice style="tip" title="Tip: Simple container run" %}} 
We've included a super simple shell script to run your container image with arguments 
```shell
    ./scripts/docker_run.sh server [prod | dev]
```
Choose your CLI argument depending on what you want Hugo to do:
- `server` argument to run Hugo's interactive web server
- `shell` to access the container CLI
- `build` to perform a Hugo build 
- `generate_toml` to generate hugo.toml from parameters in scripts/repoConfig.json
- `update_scripts` to update scripts to latest features 
- `prod` to use the Production container (for everyday usage with latest released container)
- `dev` to use the Development container (for testing changes to Central Repo or other background items)
{{% /notice %}}

  {{% notice style="tip" title="Full Container run command" %}}

```shell
  docker run --rm -it \
  -v $(pwd):/home/UserRepo \
  --mount type=bind,source=$(pwd)/hugo.toml,target=/home/CentralRepo/hugo.toml \
  -p 1313:1313 fortinet-hugo:latest server
```
  {{% /notice %}}

   - '-rm' flag removes the container after it exits...freeing up resources
   - '-it' flag runs the container interactively providing prompt into the Container
   - '-v' flag creates a disk mount to the local file system available within the container OS
   - '-p' publishes container ports to the local OS (used to view the local Hugo Webserver)
   - CLI Options:
     - 'shell' subcommand for Hugo container to access the shell directly
     - 'server' subcommand for Hugo container to run the local/test webserver
     - 'build' subcommand for Hugo container to build the static website, **this is the default**  
  
- the 'shell argument runs the container and logs you into the container [Alpine Linux OS CLI](https://github.com/klakegg/docker-hugo/tree/master) (general Linux commands will work, but this is a lean image so doesn't include everything)
  - Note the $(pwd) in Container OS, and list files.  You'll see you have everything needed to create your Hugo site! 
  
    ```shell
    pwd
    ls -la 
    ```
{{% notice note %}} Notice the folders from your local repo are available in the container, from the disk mounts
- /content
- /layouts
- hugo.toml

These disk mounts allow bidirectional read/write between container and local file system, and these disk mounts are the only directories that will be maintained when the container shuts down
{{% /notice %}}

- Within the container shell, you can Run Hugo virtual server to get a live view of Hugo's output 

  ```
  hugo server --contentDir /home/UserRepo/content --bind=0.0.0.0
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
```bash
docker images                                           #List all images
docker ps -a                                            #List all containers, both running and stopped
docker rmi <image-id>                                   #Remove an image
docker rmi $(docker images -aq)                         #Remove all images
docker rmi $(docker images --filter dangling=true -aq)  #Remove all images with tag <none>
docker rm <container-id>                                #Remove a container
docker rm $(docker ps -aq)                              #Remove all containers
docker builder prune                                    #Remove build cache
```
When running any of the above commands, if you get an error message indicating an image or container is being used or referenced in another image or container, you can issue the '-f' flag to force remove.

