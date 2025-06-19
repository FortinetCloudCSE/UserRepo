---
title: "Optional - Install Hugo"
linkTitle: "Optional Install Hugo"
chapter: false
weight: 10
---

{{% notice tip %}} Hugo is installed on the container so it's best to use it there.  These instructions are included for legacy learning purposes {{% /notice %}}

### Hugo Local install 

- If you're using a Mac, run the following brew install from your terminal

    ```sh
    brew install hugo 
    ```
    
    If you're using Windows, install chocolatey for windows ([follow directions here](https://chocolatey.org/install)).  Once installed run the following
    
    ```sh
    choco install hugo -confirm
    ```

- Run Hugo webserver locally to see a local version of the rendered website

    From within the root of the repo you copied onto your system
    
    ```sh
    hugo server
    ```

- Click on the URL presented after the above command finishes to view a local version of your first Hugo formatted website
    ![hugoServer](hugoServer.jpg)
    ![hugoServer](logo.svg)

### Clone Central Repo if not using a container
- Because you're not using a container, you need to clone and maintain fresh copy of [CentralRepo](https://github.com/FortinetCloudCSE/CentralRepo)
    ```shell
        git clone https://github.com/FortinetCloudCSE/CentralRepo.git --recursive LocalCopyCentralRepo          
    ```
- To pull updates later
    ```shell
        cd LocalCopyCentralRepo
        git pull -r    
    ```

### Running Hugo locally w/ CentralRepo + UserRepo
- Start in Central Repo, and use hugo webserver, pointing to proper content directory and config files
    ```shell
      cd LocalCopyCentralRepo 
      hugo server --contentDir $(PWD)/../UserRepo/content --config $(PWD)/../UserRepo/hugo.toml -p 8080
    ```
  - Flags:
    - '--contentDir': tell Hugo where the /content folder is
    - '--config': tell Hugo where the frontmatter config file is
    - '-p': tell Hugo webserver what port to use
  - Hugo will serve up a local version of the page at: [http://localhost:8080/UserRepo/](http://localhost:8080/UserRepo/)

- Now that you have Hugo running locally, you can proceed to [content creation with Hugo](../02hugo.html)

- When you're ready to perform a final 'hugo build' on your site, be sure to use the '-d' flag to write files back into your UserRepo
```shell
  hugo --minify -d $(PWD)/../UserRepo/docs --contentDir $(PWD)/../UserRepo/content --config $(PWD)/../UserRepo/hugo.toml --cleanDestinationDir
```

{{% notice warning %}}
<p style='text-align: left;'>
The examples and sample code provided in this workshop are intended to be consumed as instructional content. These will help you understand how various Fortinet services can be architected to build a solution while demonstrating best practices along the way. These examples are not intended for use in production environments without full understanding of how they operate.
</p>
{{% /notice %}}