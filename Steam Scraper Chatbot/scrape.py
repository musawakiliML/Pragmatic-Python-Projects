# importing packages
import requests
import lxml.html
import json

# Getting page information, and extracting html document
html_page = requests.get('https://store.steampowered.com/explore/new/')
page_doc = lxml.html.fromstring(html_page.content)


def popular_release():
    ''' This Function extracts popular game information from Steam website.

    The functions returns a list containing a dictionary with following keys:values pair
    title: game title
    tags: category of the game
    price: price of the game
    total_platform: platforms supporting the game(win, mac, linux etc.)
    game_link: link to the game
    image_link: link to image of the game
     '''

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

    # split tags into a list
    tags = [tag.split(', ') for tag in tags]

    # get game platform
    platform_divs = new_releases.xpath('.//div[@class="tab_item_details"]')
    total_platforms = []

    # loop through the platforms and create list for each game
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

    # loop through the images link tag and extract the src attribute
    for x in images_links:
        image = x.attrib['src']
        game_images.append(image)

    # get game link
    links = new_releases.xpath('//*[@id="tab_newreleases_content"]/a')  # [1]
    game_links = []

    # loop through the game links and extract the href attribute
    for i in links:
        link = i.attrib['href']
        game_links.append(link)

    # generate output function
    popular_releases_output = []
    count = 0
    # using zip function to create a list of all the the information we need for a particular game.
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
    return popular_releases_output


# save output to json file
def save_output_json(data):
    with open("output_file.json", 'w') as file_object:
        json.dump(data, file_object)
