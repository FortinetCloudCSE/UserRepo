---
title: "Task 2 - Create/Modify MD pages"
menuTitle: "b: MD Pages"
chapter: false
weight: 2
---

### Task 2 - create or copy Markdown pages for each task within the chapter 

1. Each Chapter can have 1 or more tasks which should be completed by the participants 
2. Naming of the task Markdown pages doesn't matter, and is only used to aid the content author in organizing the content.
    {{% notice info %}} Note that the filename doesn't matter other than to help organize content.  The Title and Weight dictate the leftnav visual and ordering of the pages.  Lower weight pages are displayed first{{% /notice %}}
    ![taskPage](taskPage.png)


{{% notice warning %}} Because the file and folder names are very similar in our example repo, it can become confusing to know where to make edits.  Make sure you're editing the correct file in your IDE/editor {{% /notice%}}

3. This page contains several useful markdown shortcodes you can use for visual pop-outs on the the site

###  [Lots of shortcodes & Features available here]("https://mcshelby.github.io/hugo-theme-relearn/shortcodes/index.html")

- [Badges]("https://mcshelby.github.io/hugo-theme-relearn/shortcodes/badge/index.html"): 

    {{% badge %}}Important{{% /badge %}}
    {{% badge style="primary" title="Version" %}}6.6.6{{% /badge %}}
    {{% badge style="red" icon="angle-double-up" %}}Captain{{% /badge %}}
    {{% badge style="info" %}}New{{% /badge %}}
    {{% badge color="fuchsia" icon="fab fa-hackerrank" %}}Awesome{{% /badge %}}

- [Icons]("https://mcshelby.github.io/hugo-theme-relearn/shortcodes/icon/index.html"):

    :star: Tips this is a star
    :bulb: this is a lightbulb
    {{% icon icon="exclamation-triangle" %}}
    {{% icon icon="angle-double-up" %}}
    {{% icon icon="skull-crossbones" %}}

- [Notices]("https://mcshelby.github.io/hugo-theme-relearn/shortcodes/notice/index.html")

    {{% notice note %}} Make sure you use the *--recurse-submodules* tag so that you get all the underlying resources that allow the framework to operate properly {{% /notice %}}
    {{% notice tip %}} this is a tip box {{% /notice %}}
    {{% notice info %}} this is a tip box {{% /notice %}}
    {{%notice warning %}} The examples and sample code provided in this workshop are intended to be consumed as instructional content. These will help you understand how various Fortinet and Azure services can be architected to build a solution while demonstrating best practices along the way. These examples are not intended for use in production environments without full understanding of how they operate. {{% /notice %}}

- [Expandable sections]("https://mcshelby.github.io/hugo-theme-relearn/shortcodes/expand/index.html")":

    {{% expand title="Expand me..." %}}Thank you!{{% /expand %}}

- [Buttons]("https://mcshelby.github.io/hugo-theme-relearn/shortcodes/button/index.html"):

    {{% button href="https://gohugo.io/" %}}Get Hugo{{% /button %}}
    {{% button href="https://gohugo.io/" style="warning" icon="dragon" %}}Get Hugo{{% /button %}}

- [Mermaid (diagrams & charts)]("https://mcshelby.github.io/hugo-theme-relearn/shortcodes/mermaid/index.html"):

    ```mermaid { align="center" zoom="true" }
        graph LR;
            If --> Then
            Then --> Else
    ```

    {{< mermaid >}}
%%{init:{"theme":"forest"}}%%
graph LR;
    A[Hard edge] -->|Link text| B(Round edge)
    B --> C{<strong>Decision</strong>}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
{{< /mermaid >}}


{{< mermaid >}}
%%{init:{"fontFamily":"monospace", "sequence":{"showSequenceNumbers":true}}}%%
sequenceDiagram
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
{{< /mermaid >}}