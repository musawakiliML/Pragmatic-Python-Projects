import lxml.html
import requests


html_page = requests.get(
    "https://www.sc.com/ng/important-information/daily-card-exchange-rates/")
page_info = lxml.html.fromstring(html_page.content)

#page_title = page_info.xpath("/html/body/embed/")
page = page_info.xpath('//*[@id="content"]/embed/@original-url')
title = page_info.xpath('/html/head/title/text()')
# print(page_title)
print(page)
print(title)
