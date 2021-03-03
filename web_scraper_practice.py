from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com")

#Above is setting up the webscraper 

search = driver.find_element_by_name("q")
time.sleep(2)
search.send_keys("gme stock")

search.send_keys(Keys.RETURN)


main = driver.find_element_by_id("rcnt")
stock_value = driver.find_element_by_class_name("IsqQVc.NprOob.XcVN5d")

print('\n')
print('\n')
print("The new stock price is " + stock_value.text)
print('\n')
print('\n')
time.sleep(10)

driver.quit()