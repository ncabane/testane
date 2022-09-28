from audioop import add
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

# Opens Linkedin homepage without login in
driver = webdriver.Chrome()
driver.get('http://automationpractice.com/index.php/')

# Clicks on Women category
time.sleep(1)
clkWomen = driver.find_element(By.LINK_TEXT, 'WOMEN')
clkWomen.click();

# Clicks on Tops subcategory
time.sleep(1)
clktTops = driver.find_element(By.LINK_TEXT, 'TOPS')
clktTops.click();

# Clicks on T-shirts category
time.sleep(1)
clkTshirt = driver.find_element(By.LINK_TEXT, 'T-SHIRTS')
clkTshirt.click();

# Clicks on Add to cart
time.sleep(1)
addCart = driver.find_element(By.XPATH,'//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]')
addCart.click();

# Proceeds to checkout
time.sleep(3)
proCheck = driver.find_element(By.LINK_TEXT, 'Proceed to checkout')
proCheck.click();