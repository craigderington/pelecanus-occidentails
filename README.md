### Pelican Static Site Generator
A simple, Python-based static site generator for creating blogs and websites.


#### Overview
Pelican converts Markdown or reStructuredText content into static HTML. It supports themes, blog posts, pages, and various content formats.
Installation
Install Pelican and Markdown via pip:
pip install pelican markdown

Basic Configuration
Create a pelicanconf.py file in your project root with the following settings:

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

AUTHOR = 'Your Name'
SITENAME = 'Your Site Name'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation (optional)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://x.com/yourusername'),)

DEFAULT_PAGINATION = 10

# Theme
THEME = 'Flex'

# Uncomment to enable plugins
# PLUGINS = ['i18n_subsites']
```

#### Directory Structure

```
Directory Structure
Set up your project:
your_project/
├── content/
│   ├── pages/
│   │   └── about.md
│   └── articles/
│       └── first-post.md
├── pelicanconf.py
└── output/


content/: Store Markdown or reStructuredText files.
pages/: Static pages like "About".
articles/: Blog posts.
output/: Generated HTML files.
```

#### Creating Content
```
Example blog post (content/articles/first-post.md):
Title: My First Post
Date: 2025-07-14 12:00
Category: Blog

Welcome to my first Pelican post!
```

```
Example page (content/pages/about.md):
Title: About
Slug: about
Date: 2025-07-14

This is my site built with Pelican.
```

#### Running the Server

Generate the site:
```
pelican content -o output -s pelicanconf.py
```

Run the development server:
```
pelican --listen --autoreload
```

Open http://localhost:8000 in your browser.


#### Additional Commands

Watch for changes:

```
pelican -r content -o output -s pelicanconf.py
```


#### Publish to production:

Update pelicanconf.py with SITEURL = "https://yourdomain.com" and run:
```
pelican content -o output -s pelicanconf.py
```


#### Resources

[Pelican Documentation](https://docs.getpelican.com/en/latest/)

[GitHub Repository](https://github.com/craigderington/pelecanus-occidentails)

