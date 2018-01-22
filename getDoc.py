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
               "Accept": "*/*"}
    url = "https://cloud.tencent.com/document/product/213/2180"
    try:
        html = session.get(url, headers=headers)
    except URLError as e:
        if hasattr(e, 'reason'):
            print ("We failed to reach a server.")
            print ("Reason: ", e.reason)
        elif hasattr(e, 'code'):
            print ("The server couldn\'t fulfill the request.")
            print ("Error code: ", e.code)
    bsObj = BeautifulSoup(html, "html5lib")
    uppper = bsObj.findAll("span", {"class": "feedback-down-count"})
    downer = bsObj.findAll("span", {"class": "feedback-up-count"})
    print(bsObj)
    print(bsObj.title)
    print(uppper)
    print(downer)


getLinks("")
