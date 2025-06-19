---
title: "Docker Helpful Hints"
linkTitle: "Docker helpful hints"
weight: 15
---

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
