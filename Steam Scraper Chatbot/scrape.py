from cmath import inf
from hashlib import new
from platform import platform
import requests
import lxml.html

# Getting page information, and extracting html document
html_page = requests.get('https://store.steampowered.com/explore/new/')
page_doc = lxml.html.fromstring(html_page.content)

new_releases = page_doc.xpath('//div[@id="tab_newreleases_content"]')[0]


titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
final_prices = new_releases.xpath(
    './/div[@class="discount_final_price"]/text()')


tags_divs = new_releases.xpath('.//div[@class="tab_item_top_tags"]')
tags = []

for div in tags_divs:
    tags.append(div.text_content())

tags = [tag.split(', ') for tag in tags]
platform_divs = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []

for game in platform_divs:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in temp]

    if "hmd_separator" in platforms:
        platforms.remove("hmd_separator")
    total_platforms.append(platforms)


popular_releases_output = []
count = 0

for info in zip(titles, final_prices, tags, total_platforms):
    resp = {}
    count = count + 1
    resp['id'] = count
    resp['title'] = info[0]
    resp['price'] = info[1]
    resp['tags'] = info[2]
    resp['platforms'] = info[3]

    popular_releases_output.append(resp)


# get images links
# get game link


links = new_releases.xpath('//*[@id="tab_newreleases_content"]/a[1]')
print(links)

# print(popular_releases_output)
