---
title: "Task 2 - Container build"
menuTitle: "b: Container Build"
weight: 5
---

## Task 2 Build a FortinetHugo container

- You only need to build the container once or if you want to ensure you have an updated CentralRepo (or if you cleared all images).
- Once Built, you can re-run the container whenever you wish to keep creating content and reviewing your Hugo site
    {{% notice warning %}} You can choose your own container name <fortinet-hugo> is used in the example below.  The name MUST be **_lowercase_** only {{% /notice %}} 
    {{% notice tip %}} The Full commands and explanation for building and running docker are listed below.  We've also included a shell script in this repo to perform the build 
    ```
        ./scripts/docker_build.sh
    ```
    {{% /notice  %}}

    ```shell
        docker build -t fortinet-hugo -f DockerfileContentCreation .
   ```
   
    - The container image is a point-in-time Ubuntu OS including s a Hugo installation and cloned CentralRepo so your Hugo formatting/themes/branding will always be up-to-date
      - [**_CentralRepo_**](https://github.com/FortinetCloudCSE/CentralRepo) contains necessary files, directories, and Fortinet-specific customizations to configure Hugo, it won't change often 
    - Command Line arguments
      - '-t': container_image_name, must be lowercase
      - '-f': container build filename.  Default is 'Dockerfile'
    - If you would prefer local Hugo install/development [follow these directions](localhugoinstall.html)
    - Container advantages:
      - no need to install/maintain Hugo locally
      - no need to clone/maintain Hugo "supporting files/directories"....your repo will be much larger and will get out-of-date quickly
      - same container can be used to preview and build EVERY TECWorkshop, and you could build/move it anywhere
      - no need to rename/modify Hugo's public folder after builds
    