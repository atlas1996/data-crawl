from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options)

# driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver')
driver.get("http://weather.com.cn/radar")
pageSource = driver.page_source
bsObj = BeautifulSoup(pageSource, "lxml")
cityList = bsObj.findAll("a", href="#")
for city in cityList:
    print(city)
