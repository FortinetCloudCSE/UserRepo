---
title: "Task 4 - image storage"
linkTitle: "Images"
chapter: false
weight: 4
---

### Image Storage

- Option 1: use externally fully qualified absolutely path (this can be a pain)
- Option 2: if you have a directory with all your images.... 
  - put it in "/content/images"
  - MD usage(from a chapter page in "content/chapter01") 
    ```
        ![Magic](../images/magic.gif)
    ```
- Option 3:  I find it easier to organize images with the pages they go with (this is how the template repo is setup
  - put images in the chapter directory
    - e.g. images in "/content/chapter1/"
      - MD Usage:
        ```
            ![Magic](magic.gif)
        ```