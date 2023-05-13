---
title: "Task 2 - Container build"
menuTitle: "b: Container Build"
weight: 5
---

## Task 2 Build a FortinetHugo container

- this is a 1 time action, only necessary the first time you create a repo
    {{% notice info  %}} The container is built with your GitHub SSH keys, so depending on your OS and how you created the keys, the arguments below may change. 
    Usually, the key files are named with either **id_ed25519** OR **id_rsa**
    {{% /notice %}}

    {{% notice warning %}} Container name <fortinet-hugo> in the example below MUST be **_lowercase_** only {{% /notice %}}
    
    {{% notice tip %}} The Full commands and explanation for building and running docker are listed below.  We've also included a shell script in this repo to run the commands  
    - MacOS/using ed25519 keys
      ```
      ./scripts/docker_cmd_ed25519.sh
        ```
    - using RSA keys:
        ```
        /scripts/docker_cmd_rsa.sh
        ```

    {{% /notice  %}}

    ```shell
   docker build -t fortinet-hugo \
   --build-arg ssh_prv_key="$(cat ~/.ssh/id_ed25519)" \
   --build-arg ssh_pub_key="$(cat ~/.ssh/id_ed25519.pub)" \
   -f DockerfileContentCreation .

   ```
   
    - The container image is a point-in-time Ubuntu OS including s a Hugo installation and cloned CentralRepo so your Hugo formatting/themes/branding will always be up-to-date
      - [**_CentralRepo_**](https://github.com/FortinetCloudCSE/CentralRepo) contains necessary files, directories, and Fortinet-specific customizations to configure Hugo, it won't change often 
    - If you would prefer local Hugo install/development follow these directions <link and readme ToBeCreated>
    - Container advantages:
      - no need to install/maintain Hugo locally
      - no need to clone/maintain Hugo "supporting files/directories"....your repo will be much larger and will get out-of-date quickly
      - same container can be used to preview and build EVERY TECWorkshop, and you could build/move it anywhere
      - no need to rename/modify Hugo's public folder after builds
    