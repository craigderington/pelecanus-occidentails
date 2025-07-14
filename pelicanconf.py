from datetime import datetime

AUTHOR = "Craig Derington"
SITENAME = "My Linux Notebook"
SITEURL = "http://localhost:8000"
#SITEURL = "https://notes.craigderington.dev"
SITESUBTITLE = "My Linux Notebook"
SITEDESCRIPTION = "My Computer Programming Notebook "
SITELOGO = "/images/craig-128x128.png"
THEME = "Flex"
FAVICON = "/images/favicon.ico"
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"
PATH = "content"
STATIC_PATHS = ["images"]
DEFAULT_PAGINATION = 5
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
USE_LESS = True
TIMEZONE = "America/New_York"
I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"
COPYRIGHT_YEAR = datetime.now().year
DATE_FORMATS = {
    "en": "%B %d, %Y",
}

# Articles
ARTICLE_URL = "{slug}.html"
DISABLE_URL_HASH = True

# Feed generation is usually not desired when developing

FEED_ATOM = "feeds/{slug}.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = "feeds/{slug}.atom.xml"
AUTHOR_FEED_RSS = "feeds/{slug}.rss.xml"

# GitHub 
GITHUB_CORNER_URL = "https://github.com/craigderington"

# Social
SOCIAL = (
    ("github", "https://github.com/craigderington"),
    ("docker", "https://hub.docker.com/u/craigderington"),   
    ("python", "https://craigderington.dev"),
    ("java", "https://craigderington.github.io"),
    ("btc", "https://strike.me/cderington17"),
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}
