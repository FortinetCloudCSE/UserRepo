---
title: "Updating the Jenkins Personal Access Token"
linkTitle: "Updating the Jenkins PAT"
chapter: false
weight: 1
---

### The Jenkins PAT

The Jenkins personal access token is used by Jenkins to retrieve Git repo information and send status checks during pipeline runs.

To generate a new token, navigate a web browser to the team [Github](https://github.com/FortinetCloudCSE), and click the <img src="fct-logo.png" alt="gh-logo" style="width: 30px; display: inline;"> at the top right of the screen.

![UserIconClick](github-main-page.png)

Click 'Settings' in the dropdown.

![SettingsClick](icon-dropdown.png)

At the bottom left of the ***Settings*** page, click 'Developer Settings.'

![DevSettingsClick](dev-settings-click.png)

Click the 'Personal access tokens' dropdown, and click 'Tokens (classic)'.

![PATClick](pat-click.png)

### Generating a New Token

To generate a new token, follow these steps. If you just need to regenerate an existing token, skip down to the following section.

To generate a new token, click the 'Generate new token' dropdown near the top right of the ***Personal access tokens (classic)*** screen. In the dropdown, click 'Generate new token (classic).'

![GNTDropdown](gnt-dropdown.png)

You will be prompted to enter your FortiAuthenticator TOTP code. Enter it, and on the ***New personal access token (classic)*** page, ensure the following permissions are checked:

- ***repo*** and all of its sub-options:

  ![RepoPerms](repo-perms.png)

- ***admin:repo_hook*** and all of its sub-options:

  ![AdminPerms](admin-perms.png)


Choose an expiration date, optionally add a note, and click <img src="gen-token-button.png" alt="gen-tkn" style="width: 100px; display: inline;"> at the bottom of the screen.

***Note: When the token appears on the next screen, ensure you copy and paste it somewhere where you can retrieve it before navigating away from the screen or closing the tab. Once you do, you will not be able to retrieve the token again and will need to generate another.***

### Regenerating an Existing Token

To regenerate an existing token, from the ***Personal access tokens (classic)*** screen, click the name of the token. For example:

![PATTokenExample](pat-token-example.png)

On the following screen, ensure the requisite permissions are selected, and click 'Regenerate token', and copy the token someplace handy where you can retrieve it later.

![RegenToken](regen-token.png)


### Updating Jenkins

Navigate to the FortinetCloudCSE Jenkins [server](https://jenkins.fortinetcloudcse.com:8443), and login with your credentials. To update a token, you'll need admin permissions.

![Jenkins-login](jenkins-login.png)

After logging in, click 'Manage Jenkins' on the left hand side of the screen.

![ManageJenkins](manage-jenkins.png)

On the ***Manage Jenkins*** screen, under the ***Security*** heading, click 'Credentials'.

![ClickCredsJenkins](click-creds-jenkins.png)

On the ***Credentials*** page, click the name of the token you want to update. Then, click 'Update' on the left menu.

![UpdateToken](update-token.png)

Click 'Change Password', paste in the new token, and click <img src="jenkins-save-btn.png" alt="jenk-sv-btn" style="width: 100px; display: inline;">.

### Confirm the token works

Click the 'Manage Jenkins' breadcrumb at the top of the screen.

![MJBreadcrumb](mj-breadcrumb.png)

Click 'System' under the ***System Configuration*** heading on the ***Manage Jenkins*** page. 

![MJSystem](mj-system.png)

Scroll down to the ***Github*** section towards the center of the page.

![GithubServers](github-servers.png)

Select the credential that references the token you just updated, and click <img src="test-conn-btn.png" alt="test-conn-btn" style="width: 100px; display: inline;">.

If the token is valid and working, you should see a message appear such as **Credentials verified for user...** as in the image below.

![CredsVer](creds-ver.png)


