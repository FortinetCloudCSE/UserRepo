# Template Repo for Unique Hugo Content

This is the sample repo which will become the Template repo we will use to create new/individual repos from 

Process

   - Clone and work in [User Repo]("https://github.com/FortinetCloudCSE/UserRepoTest") (which will ultimately be the Template repo)
     - Content (chapters with MD)
     - Scripts 
     - Static
     - Config.toml
     - Dockerfiles
   - Container Build with DockerfileBuild, then run 
       ```
       docker build -t myHugoDevContainer -f DockerfileBuild .
       docker run -p 1313:1313 myHugoDevContainer:latest
       ```
     - In a browser, navigate to: http://localhost:1313/DemoFrontEnd/
       - Container pulls in [Central Repo]("https://github.com/FortinetCloudCSE/CentralRepoTest") (which is where we'll make any template changes)
       - Container (ideally) displays local version of Hugo site updating near real time as you create content	
     - When satisfied with Hugo content, Container build with *DockerFileTest*
       ```
       docker build -t myHugoPubContainer -f DockerfileTest .
       docker run myHugoPubContainer:latest
       ```
       - Container outputs /public folder which is the result from "Hugo build"
         - This /public folder can be hosted anywhere.  We'll still use GH Pages to host the actual page.

   