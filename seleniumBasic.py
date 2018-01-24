from selenium import webdriver
from bs4 import BeautifulSoup


# REPLACE WITH YOUR DRIVER PATH. EXAMPLES FOR CHROME AND PHANTOMJS
driver = webdriver.Chrome()
# driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver')
driver.get("https://cloud.tencent.com/document/product/213/2180")

pageSource = driver.page_source
bsObj = BeautifulSoup(pageSource, "lxml")

uppper = bsObj.find("span", {"class": "feedback-down-count"})
downer = bsObj.find("span", {"class": "feedback-up-count"})

print(bsObj.title.string)
print(uppper.string)
print(downer.string)
driver.close()
