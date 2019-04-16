from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get('http://google.com')

body = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.get('http://bing.com')
time.sleep(3)

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+Keys.PAGE_UP)
time.sleep(2)

driver.find_element_by_tag_name(body).send_keys(Keys.CONTROL+'W')
