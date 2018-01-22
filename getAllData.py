from selenium import webdriver
from bs4 import BeautifulSoup
import re

pages = set()
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options)


def markdownParser(bsObj):
    markdown = bsObj.find("div", {"class": "markdown-text-box"})
    print(markdown.h1.text)
    print(markdown.findAll("h2").count)

def getData(pageUrl):
    global pages
    # REPLACE WITH YOUR DRIVER PATH. EXAMPLES FOR CHROME AND PHANTOMJS
    # driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver')
    driver.get("https://cloud.tencent.com"+pageUrl)
    pageSource = driver.page_source
    bsObj = BeautifulSoup(pageSource, "lxml")
    try:
        print(bsObj.find("span", {"class": "feedback-down-count"}).string)
        print(bsObj.find("span", {"class": "feedback-up-count"}).string)
    except AttributeError:
        print("there is something missing")
    markdownParser(bsObj)

    for link in bsObj.findAll("a", {"class": {"product-detail",
                                              "side-nav-title-2",
                                              "side-nav-title-1",
                                              }}):
        if 'href' in link.attrs and link.attrs['href'] != "javascript:;":
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                pages.add(newPage)
                getData(newPage)


getData("/document/product/213/492")
