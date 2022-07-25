import requests
import lxml.html

# Getting page information, and extracting html document
html_page = requests.get('https://store.steampowered.com/explore/new/')
page_doc = lxml.html.fromstring(html_page.content)
