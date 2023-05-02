var relearn_search_index = [
  {
    "content": "Fortinet Standard Workshop Web format - MVP1 Welcome! This site, hosted on GitHub Pages, will explain how to use the Hugo Web Framework “Learning Theme” to effectively deliver Fortinet Product demos in a constent, simple, and visually appealing format.\nThe beauty of this framework lies in its simplicity. Within approx 30 mins, anybody can have a site up and running. Content is created via Markdown files, and the course layout is simply a folder structure.\nFollow along on this simple tutorial to get up and running with a Hugo formatted site for your training/demo content today!\nLearning Objectives Setup hugo on your system and clone this repo for re-usable starting point Customize the Hugo content folder to display proper information flow for your content/demo/training Publish your Hugo site to GitHub pages via a CI/CD model (GitHub action will automatically re-build your Hugo content whenever you push to the underlying repo) About Hugo and Fortinet TECRecipies !!!!!!!!!!!!!! RECREATE NEW CONTENT FOR EVERYTHING BELOW HERE !!!!!!!!!!!!! ",
    "description": "",
    "tags": null,
    "title": "Fortinet Standard Workshop Web format - MVP1",
    "uri": "/index.html"
  },
  {
    "content": "Task 1 - Create a Folder structure correlating to the major topics/sections of the demonstration Browse to the content directory within this repo The Left Hand navigation menu is driven by the folder structure you create Chapters are ordered according to the number prefix on the folder Folder Naming doesn’t appear on the published site, it only helps the content creator organize the chapters \u0026 remember what’s in each Chapter Within each folder there is an _index.md file which is used to create the content of the Chapter header page The _index.md is used to\ntitle the Chapter header page in left hand navigation display chapter introduction content on the chapter heading page Notice the folder structure and file naming on the left and the resulting display on the right Info Note that the file and folder names only matter for ordering. Lower numbered folders will appear first. Only the \"title\" tags within each Markdown file will impact the resulting page view Subsequent Markdown pages under each folder are used to house tasks/steps within each chapter ",
    "description": "",
    "tags": null,
    "title": "Task 1 - Chapter Folder Structure",
    "uri": "/02chapter2/2_task1.html"
  },
  {
    "content": "MVP1 - in progress Task 1 - Create Repo Use the Jenkins Script with GH credentials to create a new repo in the FortinetCloudCSE GitHub account For now this is limited to Jeff \u0026 Rob ./setup-gh-jenkins \u003cYour Jenkins user id\u003e \u003cName of Repo Template\u003e \u003cName of New Repo to be created\u003e \u003cGithub username of user to be added as collaborator\u003e [-p] This script will:\nCreate a new repo in FortinetCloudCSE from the Parent Template DemoFrontEndDocker Add specified GitHub collaborators to the newly created Repo Create a Jenkins job for the repo and run initial build. This job can/will do things like linting Directory governance FortiDevSec scans MVP0 (LEGACY STEPS only do this if MVP1 steps don’t work) Task 1 - Clone this sample repo ** Prerequisite ** - Ensure Git is installted on your system\nStep 1 Clone this git repo git clone https://github.com/FortinetCloudCSE/DemoFrontEndDocker.git --recurse-submodules ",
    "description": "",
    "tags": null,
    "title": "Task 1 - Clone sample repo",
    "uri": "/01gettingstarted/2_task1.html"
  },
  {
    "content": "Task 1 - Insert Hugo content into your Parent repo We want to house the Hugo content close to the rest of your demo content (terraform/cloudformation/scripts/etc). So all you have to do is copy your hugo content into your parent repo root directory copy your entire Hugo folder DemoFrontEnd to the root of the repo you’re using for your Demo. Folder structure should look similar to the following: ",
    "description": "",
    "tags": null,
    "title": "Task 1 - Insert Hugo content into your Parent Repo ",
    "uri": "/03chapter3/2_task1.html"
  },
  {
    "content": "Task 2 - Install Hugo If you’re using a Mac, run the following brew install from your terminal\nbrew install hugo If you’re using Windows, install chocolatey for windows (follow directions here). Once installed run the following\nchoco install hugo -confirm Run Hugo locally to see a local version of the rendered website From within the root of the repo you copied onto your system\nhugo server Click on the URL presented after the above command finishes to view a local version of your first Hugo formatted website\nWarning The examples and sample code provided in this workshop are intended to be consumed as instructional content. These will help you understand how various Fortinet and Azure services can be architected to build a solution while demonstrating best practices along the way. These examples are not intended for use in production environments without full understanding of how they operate. ",
    "description": "",
    "tags": null,
    "title": "Task 2 - Install Hugo",
    "uri": "/01gettingstarted/3_task2.html"
  },
  {
    "content": "Task 2 - Push your content to GitHubo repo In a terminal window, Browse to the root within this repo git push Note You may need to first issue a **git fetch** or other actions to get your content properly uploaded to GitHub. ",
    "description": "",
    "tags": null,
    "title": "Task 2 - Push content to your repo",
    "uri": "/03chapter3/3_task2.html"
  },
  {
    "content": "Task 2 - create or copy Markdown pages for each task within the chapter Each Chapter can have 1 or more tasks which should be completed by the participants Naming of the task Markdown pages doesn’t matter, and is only used to aid the content author in organizing the content. Info Note that the filename doesn't matter other than to help organize content. The Title and Weight dictate the leftnav visual and ordering of the pages. Lower weight pages are displayed first Warning Because the file and folder names are very similar in our example repo, it can become confusing to know where to make edits. Make sure you're editing the correct file in your IDE/editor This page contains several useful markdown shortcodes you can use for visual pop-outs on the the site ⭐ Tips this is a star 💡 this is a lightbulb\nNote Make sure you use the *--recurse-submodules* tag so that you get all the underlying resources that allow the framework to operate properly Tip this is a tip box Info this is a tip box Warning The examples and sample code provided in this workshop are intended to be consumed as instructional content. These will help you understand how various Fortinet and Azure services can be architected to build a solution while demonstrating best practices along the way. These examples are not intended for use in production environments without full understanding of how they operate. ",
    "description": "",
    "tags": null,
    "title": "Task 2 - Task MD pages",
    "uri": "/02chapter2/3_task2.html"
  },
  {
    "content": "Task 2 - Adjust the config.toml file which controls overall paramaters for the site Open the config.toml file under the repo root to change a few parameters of the site Edit the baseUrl to match the GitHub Page for your site (you won’t have this until you’ve done at least 1 GitHub action/build) Add information URL’s to the bottom of the leftnav bar with [[menu.shortcuts]] menu.shortcuts are displayed lowest to highest according to their weight Additional customizations can be made with themeVariants, but they won’t be covered here ",
    "description": "",
    "tags": null,
    "title": "Task 3 - Adjust config.toml site settings",
    "uri": "/02chapter2/4_task3.html"
  },
  {
    "content": "Task 3 - Create GitHub action for Hugo Publish Warning You must have proper repo permissions to setup a GitHub action. If you do not see the settings button on the top repo banner/ribbon, please reach out to the repo owner to get the proper permissions In your web browser, navigate to the GitHub repo and click on Settings in the top ribbon On the left hand nav bar, click on Pages Under Source select GitHub Actions Click Browse All Workflows Search for Hugo and then click Configure under the Hugo GitHub Actions You’ll see a hugo.yml file created, which directs GitHubActions to execute a Hugo Build Command anytime the repo is updated. We need to make 1 minor adjustment to this file. B/c we located our hugo content underneath the repo root, we need to tell hugo where it needs to build and publish. Once updated per your folder naming in the spots shown below, click Start Commit Specifically, you want to add a working-directory under the jobs: –\u003e build: –\u003e steps: section and then update the Upload Artifact path. You can copy and paste this entire script into your hugo.yml file, or just edit the specific lines for working directory (in the bottom 1/3 of the file)\n# Sample workflow for building and deploying a Hugo site to GitHub Pages name: Deploy Hugo site to Pages on: # Runs on pushes targeting the default branch push: branches: [\"main\"] # Allows you to run this workflow manually from the Actions tab workflow_dispatch: # Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages permissions: contents: read pages: write id-token: write # Allow one concurrent deployment concurrency: group: \"pages\" cancel-in-progress: true # Default to bash defaults: run: shell: bash jobs: # Build job build: runs-on: ubuntu-latest env: HUGO_VERSION: 0.108.0 steps: - name: Install Hugo CLI run: | wget -O ${{ runner.temp }}/hugo.deb https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb \\ \u0026\u0026 sudo dpkg -i ${{ runner.temp }}/hugo.deb - name: Install Dart Sass Embedded run: sudo snap install dart-sass-embedded - name: Checkout uses: actions/checkout@v3 with: submodules: recursive - name: Setup Pages id: pages uses: actions/configure-pages@v2 - name: Install Node.js dependencies run: \"[[ -f package-lock.json || -f npm-shrinkwrap.json ]] \u0026\u0026 npm ci || true\" - name: Build with Hugo env: # For maximum backward compatibility with Hugo modules HUGO_ENVIRONMENT: production HUGO_ENV: production run: | hugo \\ --minify \\ --baseURL \"${{ steps.pages.outputs.base_url }}/\" working-directory: ./hugeowebfront - name: Upload artifact uses: actions/upload-pages-artifact@v1 with: path: ./hugeowebfront/public # Deployment job deploy: environment: name: github-pages url: ${{ steps.deployment.outputs.page_url }} runs-on: ubuntu-latest needs: build steps: - name: Deploy to GitHub Pages id: deployment uses: actions/deploy-pages@v1 7. Click to Commit new file 8. You’ll see the new GitHub action file hugo.yml created in the .github/workflows folder of the repo. You can review the action to see results of the build ",
    "description": "",
    "tags": null,
    "title": "Task 3 - Create GitHub action for Hugo Publish",
    "uri": "/03chapter3/4_task3.html"
  },
  {
    "content": "Hugo - Getting started Chapter 1 - Setting up your Hugo environment (15 min) What is Hugo and how easy can this be? Generally, this section follows the example set forth here\nClick the right arrow to go through each step individually\n",
    "description": "",
    "tags": null,
    "title": "Ch 1 Getting Started with Hugo",
    "uri": "/01gettingstarted.html"
  },
  {
    "content": "Learn to organize and create content in Hugo- estimated duration 20min With Hugo installed, you can proceed to creating and editing your demonstration content.\nHugo is incredibly powerful and allows many customizations, and we won’t cover most of theme here as they’ve already been set for Fortinet’s standard template\nGenerally, you only need to do 3 things:\nSet the folder structure for left hand menu bar navigation/topic structure Create Markdown files for each task within the Chapter/topics Adjust the site’s settings via config.toml Click the right arrow to go through each step individually\n",
    "description": "",
    "tags": null,
    "title": "Ch 2 Hugo Content Structure",
    "uri": "/02chapter2.html"
  },
  {
    "content": "Publish your content to GitHub pages via a GitHub action Now that you have your content first draft, push your repo to github, and setup an action to automatically build your Hugo content anytime you upload to the repo\nClick the right arrow to go through each step individually\n",
    "description": "",
    "tags": null,
    "title": "Ch 3 - Hugo Publish via GitHub Actions (CI/CD)",
    "uri": "/03chapter3.html"
  },
  {
    "content": "",
    "description": "",
    "tags": null,
    "title": "Categories",
    "uri": "/categories.html"
  },
  {
    "content": "",
    "description": "",
    "tags": null,
    "title": "Tags",
    "uri": "/tags.html"
  }
]
