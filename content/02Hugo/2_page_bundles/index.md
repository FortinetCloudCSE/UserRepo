---
title: "Task 2 - Hugo Page Bundles"
linkTitle: "Page Bundles"
weight: 20
---

{{% badge style="info" color="orange" icon="fa-fw fas fa-exclamation-triangle" title=" " %}}Change{{% /badge %}}
{{% badge style="info" icon="fa-solid fa-circle-plus" title=" " %}}New{{% /badge %}}

### What is a Hugo Page Bundle?

In an effort to better organize and stadardize image storage and display, and to simplify image references in Markdown, Hugo introduced [Page Bundles](https://gohugo.io/content-management/page-bundles/).

A Hugo Page Bundle is a directory that contains a content file (e.g., `index.md` or `_index.md`) and its associated resources (e.g., images, videos, documents). This structure allows you to keep all related files together, making it easier to manage and reference them.

### Why use Hugo Page Bundles?
- **Organization**: Keeps related content and resources together, making it easier to manage.
- **Simplified References**: Allows for simpler relative paths to resources, reducing the chances of broken links.
- **Portability**: Makes it easier to move or copy content along with its resources.
- **Scalability**: Facilitates the addition of new content and resources without cluttering the main content directory. 

### How to create a Hugo Page Bundle
1. Create a directory for your content. The directory name can be anything, but it's often helpful to use a descriptive name.
2. Inside this directory, create an `index.md` file for regular pages or `_index.md` for chapter/section pages. This file will contain the content for that page or section.
3. Add any associated resources (e.g., images, videos) to the same directory.
4. Reference the resources in your Markdown file using relative paths.


### Example of a Hugo Page Bundle structure
```
my-page-bundle/
├── index.md
├── image1.png
├── image2.jpg
└── document.pdf
```     

   - For example, if you have an image named `example.png` in the same directory as your `index.md`, you can reference it like this:
     ```markdown
     ![Example Image](csemascot.png)
     ```
      
  - Even better, use the figure shortcode to avoid unnecessary clickable images

    ```markdown
      {{</* figure src="csemascot.png" */>}}
    ```

    ![Example Image](csemascot.png)

    {{< figure src="csemascot.png" >}}
  
