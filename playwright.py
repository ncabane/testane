from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get('https://playwright.dev/')

# Waits 1 second and then clicks on Get Started
time.sleep(1)
opensGetStarted = driver.find_element(By.LINK_TEXT, 'GET STARTED')
opensGetStarted.click();

# Waits 1 second and then clicks How to Install
time.sleep(1)
howToinstall = driver.find_element(By.LINK_TEXT, 'How to install Playwright')
howToinstall.click();