from textwrap import fill
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()
driver.get('https://www.megekko.nl/')

# Waits 2 seconds and then clicks OK button
time.sleep(3)
acceptCookie = driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
acceptCookie.click();

# Clicks on categories
time.sleep(2)
catOpen = driver.find_element(By.ID, 'searchFieldInputField')
catOpen.click();
catOpen.send_keys("Nvidia")
catOpen.send_keys(Keys.ENTER);

# Places an item in the shop cart
time.sleep(2)
addCart = driver.find_element(By.CLASS_NAME, 'shopbutton')
addCart.click();

# Fills email field
time.sleep(2)
fillEmail = driver.find_element(By.ID, 'email')
fillEmail.click();
fillEmail.send_keys("testane@testane.com")

# Selects country Nederland
time.sleep(2)
seLand = driver.find_element(By.ID, 'land')
seLand.click();
time.sleep(2)
seLand.click();




