from urllib.request import urlopen, URLError
from bs4 import BeautifulSoup
import requests
import re
import ssl

page = set()
ssl._create_default_https_context = ssl._create_unverified_context


def getLinks(pageUrl):
    global pages
    session = requests.Session()
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\
                              AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9\
                          ,image/webp,*/*;q=0.8"}
    url = "https://cloud.tencent.com/document/product/213/492"
    try:
        html = session.get(url, headers=headers)
    except URLError as e:
        if hasattr(e, 'reason'):
            print ("We failed to reach a server.")
            print ("Reason: ", e.reason)
        elif hasattr(e, 'code'):
            print ("The server couldn\'t fulfill the request.")
            print ("Error code: ", e.code)
    bsObj = BeautifulSoup(html.content, "lxml")
    uppper = bsObj.find("span", {"class": "feedback-down-count"}).string
    downer = bsObj.find("span", {"class": "feedback-up-count"}).string
    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            if link.attrs['href'] not in page:
                newPage = link.attrs['href']
                print(newPage)
                print(bsObj.title)
                print(uppper)
                print(downer)
                page.add(newPage)
                getLinks(newPage)


getLinks("")
