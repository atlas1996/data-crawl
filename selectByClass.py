from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
html = urlopen("https://cloud.tencent.com/document/product/213/2180")
bsObj = BeautifulSoup(html, "html5lib")
nameList = bsObj.findAll("span", {"class": "feedback-down-count"})
for name in nameList:
    print(name)
