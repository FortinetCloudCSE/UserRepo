---
title: "Task 5 - Shortcodes & Partials"
linkTitle: "Shortcodes & Partials"
chapter: false
weight: 5
---

### Partials - Site customization (rarely used)

- /layouts/partials are customizations used to tweak overall CSS parameters of the site.  Generally these are reserved for use by ALL repos and can be changed by emailing [Fortinet Cloud CSE team](mailto:fortinetcloudcse@fortinet.com)
- If you absolutely must change something, use [Hugo Partials](https://gohugo.io/templates/partials/) as your guide
- Partials are automatically included in the site's CSS configuration

### Shortcodes - custom HTML 

- If you need to use complex and/or custom HTML in your guide, or you have an often repeated bti of HTML you want to user across your markdown, you can use a custom shortcode.
- /layouts/shortcodes/<insertFileName.html>
- [Hugo Shortcodes Documentation] (https://gohugo.io/extras/shortcodes/)
- Custom Shortcodes are referenced inline your markdown
- The [index.md](https://github.com/FortinetCloudCSE/UserRepo/blob/main/content/_index.md) page of this guide includes a shortcode for an image with embedded URLs (Created in diagrams.net)
  - This shortcode example is included in your cloned repo at [/layouts/shortcodes/FTNThugoFlow.html](https://github.com/FortinetCloudCSE/UserRepo/blob/main/layouts/shortcodes/FTNThugoFlow.html)
  - Other shortcode examples in [CentralRepo](https://github.com/FortinetCloudCSE/CentralRepo/tree/main/layouts/shortcodes)
  - Simple shortcode to insert a RED Fail or GREEN Success: https://github.com/FortinetCloudCSE/AWS-FGT-201/tree/main/layouts/shortcodes