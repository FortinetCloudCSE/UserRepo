# Fortinet Template Repo for TECWorkshops2

## Prereqs
  - Docker
  - GitHub keys
    - Follow the instructions [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) to generate a new SSH key pair
      - {{% notice warning %}} DO NOT USE A PASSPHRASE when you create the keys{{%  /notice %}}
    - Once created follow [these directions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) to add the newly created Key to your GitHub account.

## General Workflow
1. Request a new repo for your TECWorkshop (this will be referred to as your **_UserRepo_**)
   - Send an email to [fortinetcloudcse@fortinet.com]("mailto:fortinetcloudcse@fortinet.com") to request a new GitHub repo and Jenkins Pipeline. Providing the following:
     - Repo Name <Fortinet-Product-CSP-Feature>
     - GitHub Usernames of collaborators
     - Your Fortinet email address
   - Behind the scenes, a script is used to create your TECWorkshop repo with appropriate protections and features.  Additionally a Jenkins pipeline will be setup to monitor changes to the repo and run things like 
     - publishing the web site
     - FortiDevSec scanning
       - To facilitate this, administrators will send you an Application ID that you must copy into fdevsec.yaml in order for the scans to run and tests to pass. Jenkins tests must pass in order for your feature branch to be merged into the main branch.
  - Along with the FortiDevSec application id, you will also be sent an account number which you can use to navigate to the FortiDevSEC console to view the results of your scan. 
    - To do so, head to [FortiCloud](https://support.fortinet.com) and click **IAM Login** on the left hand side of the page. Enter the provided account number along with your FortiCloud login credentials.  
  - You will use this repo to create and modify MD chapters & tasks to create your workshop Guide in Hugo format
    - Help with Git is included below
2. Build a FortinetHugo container - this is a 1 time action, only necessary the first time you create a repo
    {{% notice warning %}} **Container name <fortinet-hugo> in the example below MUST be lowercaseonly** {{% notice %}}
    
    ```shell
   docker build -t fortinet-hugo -f DockerfileContentCreation .

   ```
   
    - The container image is a point-in-time Ubuntu OS including s a Hugo installation and cloned CentralRepo so your Hugo formatting/themes/branding will always be up-to-date
      - **_CentralRepo_** contains necessary files, directories, and Fortinet-specific customizations to configure Hugo, it won't change often 
    - If you would prefer local Hugo install/development follow these directions <link and readme ToBeCreated>
    - Container advantages:
      - no need to install/maintain Hugo locally
      - no need to clone/maintain Hugo "supporting files/directories"....your repo will be much larger and will get out-of-date quickly
      - same container can be used to preview and build EVERY TECWorkshop, and you could build/move it anywhere
      - no need to rename/modify Hugo's public folder after builds
    
3. Run container w/ local disk mounts & create your markdown TECWorkshop Guide (repeat this procedure for any TECWorkshop you're creating) 

    ```shell
    docker run --rm -it -v $(pwd)/content/:/home/CentralRepo/content -v $(pwd)/config.toml:/home/CentralRepo/config.toml -v $(pwd)/docs:/home/CentralRepo/public  -p 1313:1313 fortinet-hugo:latest
    ```
   - '-rm' flag removes the container after it's closed...freeing up resources
   - '-it' flag provides an interactive prompt into the Container
   - '-v' flag creates a disk mount to the local file system available within the container OS
   - '-p' publishes container ports to the local OS (used to view the local Hugo Webserver)
    
- the above command runs the container and logs you into the container Ubuntu OS CLI (most Linux commands will work)
  - NOTE the $(pwd), and list files, 
  
    ```shell
    pwd
    ls -la 
    ```
  - Run Hugo virtual server to get a live view of Hugo's output 

    ```
    hugo server --bind 0.0.0.0
    ```
    In your local machine, browse to http://localhost:1313/UserRepo

4. You now have a container running hugo webserver and tracking changes to the **_/content_** directory in your repo.  

  - Create your TecWorkshop Guide including Chapers and tasks.  You can use your favorite editor/IDE to create the markdown pages
  - Depending on several factors, you may or may not see LIVE changes to the http://localhost:1313/SubDirectory page  
  - If you're not seeing live changes... re-run hugo server command on container (ctrl+C to end the running hugo process on container CLI)

{{% notice note% %}}  You do need to make a minor change to the **_config.toml_** file in this repo {{% /notice% %}}

5. When you're satisfied with Hugo view of your content in Hugo virtual server, issue a Hugo 'build' in the container CLI

    ```shell
    hugo --minify
    ```
        
   - This command "builds" your Hugo site into the container's **_/public_** folder.  We used a docker disk mount to map this folder back to your local **_/docs_** folder, so the Hugo website will automatically be copied back into your local repo
   - You can now exit the container with ctrl + cd, or command: 'exit'
   - When you exit the container, any changes you made to the container will be lost and cannot be recovered
     - **_Remember_** we edited the /content folder on our local OS, so those changes were not made to the container and will not be lost
     - Further, the disk mount from local's **_/docs_** to Container's **_public_** AUTOMATICALLY writes the hugo build to your local OS, so those changes will not be lost
     - If you need to continue editing, just run a new container from your built image, and run hugo's webserver.  Everything is linked properly so it should just work
   
6. Finally, **from your local workstation CLI**, push the newly created Hugo site up to GitHub to automatically publish your Hugo Site
   ```shell
   git add .
   git commit -m "<my commit message>"
   git push 
    ``` 
   - Remember we're always working in a Git Branch, so we'll need to issue a Pull request and merge [using this procedure]("https://updatethislink")


## GitHub Repo Getting Started (General Workflow for GitHub Repos)

1.  Once your repo and pipeline have been created, you will be provided with the GitHub repo link which you can use to clone and begin content creation. First, navigate to a desired local directory and clone the repo with the provided link:

  ```
  cd <desired parent directory>
  git clone <provided link>
  ```
2. Create a feature branch to begin working on your desired changes.

  ```
  git checkout -b <FEATURE-username-ShortDescr>
  ```

3. Check the repo status to verify the changes to be staged.

  ```
  git status
  ```

4. Stage the desired files (or issue -A (or .) for all), commit, and push.

  ``` 
  git add -A {or} git add .
  git commit -m "<add a commit message here>"
  git push
  ```
  If this is your first push to the branch, GitHub upstream doesn't know about it.  Just go ahead and use the provided command in this case to perform the push, which will create the upstream branch
  - To auto create new branches when you first push, update Git global config 

  ```shell
  git config --global --add --bool push.autoSetupRemote true
  ```


  Tip: An easy way to squash your commits is to perform a soft reset:
  ```
  git reset --soft <hash of the last commit you want to keep as is>
  git add -A
  git commit -m "<new commit message>"
  git log
  ```
  You will see the new commit on top of the one you referenced in the git reset command.

5. When you have completed your work and are ready to merge your changes into the main branch, perform an interactive rebase and force push to your branch.

  ```
  git rebase -i
  ```
  On the first screen, you may want to leave the top commit as is, and for the rest, replace the word 'pick' with an 's' for squash. Then, on the next screen, comment out the commit messages you don't want, leaving the preferred one as is. Once your PR is approved, checkout the main branch and perform a fast-forward merge and force push to complete the workflow.
  
  ```
  git checkout main
  git merge <feature branch name> --ff-only
  git push --force
  ```

### Notes:
- Inside the container, [Central Repo]("https://github.com/FortinetCloudCSE/CentralRepo") (which is where we'll make any template changes) is cloned and integrated with your repo.
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


### Git Help

- update your branch with something that's in main
```shell
git fetch origin main

```

### Retrieving Hugo Static Site Tar Archive

After each push to your branch, a Jenkins Pipeline will execute. This pipeline will execute some code tests, run a container to build your Hugo site package, store it in S3, and generate a presigned URL with limited permissions to access the object.

- Log into Jenkins and navigate to your pipeline.

- Under 'Stage View', beneath the stage titled 'Assume role and generate pre-signed url', hover over the green box, and click 'Logs'.

- Click the second log entry that begins with 'Shell Script -- set +x'.

- Click the hyperlink shaded in blue that begins with 'https://test-hugo-site-fortinetcloudcse.s3.amazonaws.com'. Your site folder will be downloaded to your laptop.
