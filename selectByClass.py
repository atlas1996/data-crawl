from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://weather.com.cn/radar")
bsObj = BeautifulSoup(html, "lxml")
cityList = bsObj.findAll("a", href="#")
with open('city.txt', 'w') as file:
    for city in cityList:
        file.write(city.string+'\n')
