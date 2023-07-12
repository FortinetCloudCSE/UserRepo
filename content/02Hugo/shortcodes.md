---
title: "Task 5 - Shortcodes & Partials"
menuTitle: "Shortcodes & Partials"
chapter: false
weight: 5
---

### Partials - Site customization (rarely used)

- /layouts/partials are customizations used to tweak overall CSS paramaters of the site.  Generally these are reserved for use by ALL repos and can be changed by emailing [Fortinet Cloud CSE team](mailto:fortinetcloudcse@fortinet.com)
- If you absolutely must change something, use [Hugo Partials](https://gohugo.io/templates/partials/) as your guide
- Partials are automatically included in the site's CSS configuration

### Shortcodes - custom HTML 

- If you need to use complex and/or custom HTML in your guide, use a custom shortcode.
- /layouts/shortcodes/<insertFileName.html>
- [Hugo Shortcodes Documentation] (https://gohugo.io/extras/shortcodes/)
- Custom Shortcodes are referenced inline your markdowd
- The [index.md](https://github.com/FortinetCloudCSE/UserRepo/blob/main/content/_index.md) page of this guide includes a shortcode for an image with embeded URLs (Created in diagrams.net)
  - This shortcode example is included in your cloned repo at [/layouts/shortcodes/FTNThugoFlow.html](https://github.com/FortinetCloudCSE/UserRepo/blob/main/layouts/shortcodes/FTNThugoFlow.html)