from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
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

