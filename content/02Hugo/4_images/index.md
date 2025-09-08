---
title: "Task 4 - Images & Relative Paths Links"
linkTitle: "Images & Relative Paths Links"
chapter: false
weight: 40
---

### Image Storage

- Optimal: Use Page Bundles (see previous task)
- Acceptable: Store images in a common directory and reference them with relative paths (use this if an image is used in multiple places)
- Not Recommended: Store images in the "static" directory and reference them with absolute paths (e.g., `/images/foo.png`)

### Using Images in Markdown
- Optimal: Use the Hugo `figure` shortcode to include images with optional attributes like alt text, title, width, and height.
  ```markdown
  {{</* figure src="image.png" alt="Description" title="Image Title" width="600" height="400" class="zoomable"*/>}}
  ```
- Acceptable: Use standard Markdown image syntax for simple images without additional attributes.
  ```markdown
  ![Description](image.png)
  ```
  {{< notice note >}} Markdown Image syntax results in images that are clickable and open the image file in the browser.  This is often not the desired behavior.  Use the `figure` shortcode instead and include class="zoomable" if you need to zoom in on a detailed image{{< /notice >}}


### If you need to link to different parts of your site, you can use relative paths with Page Bundles.

- Example: This page bundle is at `content/02Hugo/4_images/index.md` and you want to link to another page somewhere else in the site, you can reference it's page bundle path
  - To link to the [Chapter 1 Getting Started page]({{% ref "/01GettingStarted/" %}}): 
    ```markdown
    [sometext]({{%/* ref "/01GettingStarted/" */%}})
    ```
  - To link to a specific task within Chapter 1, e.g., [Task 3 FortiHugoRunner]({{% ref "/01GettingStarted/3_FortiHugoRunner/" %}}):
    ```markdown
    [sometext]({{%/* ref "/01GettingStarted/3_FortiHugoRunner/" */%}})
    ```
  - Example: To link to a specific task within the same Chapter, e.g., [Task 5 Shortcodes & Partials]({{% ref "5_shortcodes" %}}):
    ```markdown
    [sometext]({{%/* ref "5_shortcodes" */%}})