import requests
import lxml.html
import json

# Getting page information, and extracting html document
html_page = requests.get('https://store.steampowered.com/explore/new/')
page_doc = lxml.html.fromstring(html_page.content)

# get popular new releases
new_releases = page_doc.xpath('//div[@id="tab_newreleases_content"]')[0]

# get game title
titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
final_prices = new_releases.xpath(
    './/div[@class="discount_final_price"]/text()')

# get game tags
tags_divs = new_releases.xpath('.//div[@class="tab_item_top_tags"]')
tags = []

for div in tags_divs:
    tags.append(div.text_content())

tags = [tag.split(', ') for tag in tags]

# get game platform
platform_divs = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []

for game in platform_divs:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in temp]

    if "hmd_separator" in platforms:
        platforms.remove("hmd_separator")
    total_platforms.append(platforms)

# get images links
images_links = new_releases.xpath(
    '//*[@id="tab_newreleases_content"]/a/div/img')  # /a[1]/div[1]/img
game_images = []

for x in images_links:
    image = x.attrib['src']
    game_images.append(image)

# get game link
links = new_releases.xpath('//*[@id="tab_newreleases_content"]/a')  # [1]
game_links = []

for i in links:
    link = i.attrib['href']
    game_links.append(link)


# generate output function
popular_releases_output = []
count = 0

for info in zip(titles, final_prices, tags, total_platforms, game_images, game_links):
    resp = {}
    count = count + 1
    resp['id'] = count
    resp['title'] = info[0]
    resp['price'] = info[1]
    resp['tags'] = info[2]
    resp['platforms'] = info[3]
    resp['game_icon'] = info[4]
    resp['game_link'] = info[5]

    popular_releases_output.append(resp)


# save output to json file
with open("output_file.json", 'w') as file_object:
    json.dump(popular_releases_output, file_object)
