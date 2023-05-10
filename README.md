# Creating a New Repo and Jenkins Pipeline

## First Steps

- Follow the instructions [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) to generate a new SSH key pair, then follow [these](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) to add it to your GitHub account.

- Send an email to fortinetcloudcse@fortinet.com to request a new GitHub repo and Jenkins Pipeline. Be sure to note the desired name of the repo and the GitHub usernames of desired collaborators.

## Getting Started (General Workflow)

- Once your repo and pipeline have been created, you will be provided with the GitHub repo link which you can use to clone and being working with the repo. First, navigate to a desired local directory and clone the repo with the provided link:

```
cd <desired parent directory>
git clone <provided link>
```
- Create a feature branch to begin working on your desired changes.

```
git checkout -b <feature branch name>
```

- Check the repo status to verify the changes to be staged.

```
git status
```

- Stage the desired files (or issue -A for all), commit, and push.

``` 
git add -A
git commit -m "<add a commit message here>"
git push
```
If this is your first push to the branch, you may get a message indicating the need to set the upstream branch. Just go ahead and use the provided command in this case to perform the push.

Tip: An easy way to squash your commits is to perform a soft reset:
```
git reset --soft <hash of the last commit you want to keep as is>
git add -A
git commit -m "<new commit message>"
git log
```
You will see the new commit on top of the one you referenced in the git reset command.

- When you have completed your work and are ready to merge your changes into the main branch, perform an interactive rebase and force push to your branch.

```
git rebase -i
```
On the first screen, you may want to leave the top commit as is, and for the rest, replace the word 'pick' with an 's' for squash. Then, on the next screen, comment out the commit messages you don't want, leaving the preferred one as is. Once your PR is approved, checkout the main branch and perform a fast-forward merge and force push to complete the workflow.

```
git checkout main
git merge <feature branch name> --ff-only
git push --force
```


## Checking Your Work

- While working on your application, you may want to see what the final product may look like. To do so, you can build a container and view it in a browser.

**Container names MUST be lowercaseonly**
```
docker build -t app-test \
   --build-arg ssh_prv_key="$(cat ~/.ssh/id_rsa)" \
   --build-arg ssh_pub_key="$(cat ~/.ssh/id_rsa.pub)" \
   -f DockerfileTest .

docker run -p 1313:1313 app-test:latest
```
- In a browser, navigate to: http://localhost:1313/UserRepo

- To exit, press CTRL+D.

## Retrieving Hugo Static Site Tar Archive

After each push to your branch, a Jenkins Pipeline will execute. This pipeline will execute some code tests, run a container to build your Hugo site package, store it in S3, and generate a presigned URL with limited permissions to access the object.

- Log into Jenkins and navigate to your pipeline.

- Under 'Stage View', beneath the stage titled 'Assume role and generate pre-signed url', hover over the green box, and click 'Logs'.

- Click the second log entry that begins with 'Shell Script -- set +x'.

- Click the hyperlink shaded in blue that begins with 'https://test-hugo-site-fortinetcloudcse.s3.amazonaws.com'. Your site folder will be downloaded to your laptop.

### Notes:
- Inside the container, [Central Repo]("https://github.com/FortinetCloudCSE/CentralRepo") (which is where we'll make any template changes) is cloned and integrated with your repo.
- Container (ideally) displays local version of Hugo site updating near real time as you create content
- To run a container interactively (for troubleshooting)
  - Comment out any offending lines in the dockerfile
  - Build and run again using commands above.
  - Container outputs /public folder which is the result from "Hugo build"
    - This /public folder can be hosted anywhere.  We'll still use GH Pages to host the actual page.

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

### Git
- update your branch with something that's in main
```shell
git fetch origin
```
- Git global config to automatically create an upstream GitHub branch the first you push from a locally created branch
```shell
git config --global --add --bool push.autoSetupRemote true
```
- 
