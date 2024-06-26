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

    # Get popular new releases
    new_releases = page_doc.xpath('//div[@id="tab_newreleases_content"]')[0]

    # Get all popular game titles
    titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
    # Get all game prices
    final_prices = new_releases.xpath(
        './/div[@class="discount_final_price"]/text()')

    # Get game tags
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
    print(game_images)    
    # get game link
    links = new_releases.xpath('//*[@id="tab_newreleases_content"]/a')  # [1]
    game_links = []
    

    # loop through the game links and extract the href attribute
    for i in links:
        link = i.attrib['href']
        game_links.append(link)
    print(game_links)
    # generate output function
    popular_releases_output = []
    count = 0
    # using zip function to create a list of all the the information we need for a particular game.
    for info in zip(titles, final_prices, tags, total_platforms, game_images, game_links):
        print(game_links)
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

# get steam banner image.
def get_steam_image():
    image_request = requests.get(
        "https://m.media-amazon.com/images/I/81JXr-AQJQL._SL1500_.jpg")
    if image_request.status_code == 200:
        return image_request.url
    else:
        return None

# To-Do :
    # Steam Home page
        # New Releases
        # Specials
        # Free to play
        # SPECIAL OFFERS
        # POPULAR TAGS
        # FEATURED & RECOMMENDED
        # POPULAR VR GAMES
    # Top Selling Game
    # FEATURED DLC
    # New and Trending
    # Top Sellers
    # Whats being played
    # Upcoming
    # RECOMMENDED SPECIALS
    # Games Streaming Now
    # UNDER $10 USD
    # UPDATES AND OFFERS


# save output to json file

def save_output_json(data):
    with open("output_file.json", 'w') as file_object:
        json.dump(data, file_object)

popular_release_data = popular_release()
print(popular_release_data)
popular_release_json = save_output_json(popular_release_data)