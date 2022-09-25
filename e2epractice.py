from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

# Opens Linkedin homepage without login in
driver = webdriver.Chrome()
driver.get('http://automationpractice.com/index.php/')

# Clicks on Women category
time.sleep(2)
clkWomen = driver.find_element(By.LINK_TEXT, 'WOMEN')
clkWomen.click();

# Clicks on Tops subcategory
time.sleep(2)
clktTops = driver.find_element(By.LINK_TEXT, 'TOPS')
clktTops.click();