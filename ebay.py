from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Opens ebay.com
driver = webdriver.Chrome()
driver.get('https://www.ebay.com/')

# Accepts cookie policy
time.sleep(2)
accCookie = driver.find_element(By.XPATH, '//button[@id="gdpr-banner-accept"]')
accCookie.click();

# Clicks search bar and searches for backpack
srcBar = driver.find_element(By.XPATH, '//*[@id="gh-ac"]')
srcBar.send_keys('backpack')
srcBar.send_keys(Keys.ENTER);
