# Template Repo for Unique Hugo Content

This is the sample repo which will become the Template repo we will use to create new/individual repos from 

Full explanation below

## Quick Start
- Follow the instructions [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) to generate a new SSH key pair, then follow [these](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) to add it to your GitHub account.

- Clone this repo and Run the generate-site script to build container and create your */public* folder for publishing on web server 
```shell
git clone https://github.com/FortinetCloudCSE/UserRepoTest.git
git checkout -b Feature-<UserID>-<Description>
cd UserRepo
./scripts/generate-site.sh
```
View the Hugo generated website by opening /UserRepo/public/index.html 

### Process Explanation 

- Clone and work in [User Repo]("https://github.com/FortinetCloudCSE/UserRepo")
     - Content (chapters with MD)
     - Scripts 
     - Static
     - Config.toml
     - Dockerfiles
- Container Build with DockerfileBuild, then run the following

    **Container names MUST be lowercaseonly**
    ```
    docker build -t myhugodevcontainer -f DockerfileTest .
    docker run -p 1313:1313 myhugodevcontainer:latest
    ```
  - In a browser, navigate to: http://localhost:1313/UserRepo
    - Container pulls in [Central Repo]("https://github.com/FortinetCloudCSE/CentralRepo") (which is where we'll make any template changes)
    - Container (ideally) displays local version of Hugo site updating near real time as you create content
    - To run a container interactively (for troubleshooting)
      - Comment out any offending lines in the dockerfile
      - reBuild
      - Run in interactive mode
      ``` docker run -i -t myhugodevcontainer ```
        - to exit interactive mode ctrl+c+d 
- When satisfied with Hugo content, Container build with *DockerFileTest*
  ```
  docker build -t myHugopubcontainer -f DockerfileBuild .
  docker run myHugopubcontainer:latest
  ```
  - Container outputs /public folder which is the result from "Hugo build"
    - This /public folder can be hosted anywhere.  We'll still use GH Pages to host the actual page.
    - Docker FAQ
      - image hygiene
        - clear images
      
        ```shell
      docker rmi -f $(docker images -aq)
  ```

   ### Git Help
- update your branch with something that's in main
```shell
git fetch origin
```
- Git global config to automatically create an upstream GitHub branch the first you push from a locally created branch
```shell
git config --global --add --bool push.autoSetupRemote true
```
- 
