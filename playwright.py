from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get('https://playwright.dev/')

# Waits 1 second and then clicks on Get Started
time.sleep(1)
acceptCookie = driver.find_element(By.CSS_SELECTOR, '.lightToggleIcon_pyhR')
acceptCookie.click();

# Turns dark mode on
time.sleep(1)
darkMode = driver.find_element(By.XPATH, '/html/body/div/nav/div[1]/div[2]/div[1]/button/svg[1]')
darkMode.click();
