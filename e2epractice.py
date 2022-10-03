from audioop import add
from turtle import st
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

# Clicks on Proceeds to checkout
time.sleep(3)
proCheck = driver.find_element(By.XPATH, '//div[@id="layer_cart"]/div/div[2]/div[4]/a/span')
proCheck.click();

# Starts checkout process
time.sleep(1)
stCheck = driver.find_element(By.CSS_SELECTOR, '.standard-checkout > span')
stCheck.click();

# Account creation - Email
time.sleep(1)
accEmail = driver.find_element(By.ID, 'email_create')
accEmail.click();
accEmail.send_keys('untrux@gmail.com')

# Account creation - Proceed
time.sleep(1)
accProc = driver.find_element(By.XPATH, '//button[@id="SubmitCreate"]/span')
accProc.click();

# After the existing account erorr, closes the browser
driver.close();