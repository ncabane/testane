from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

# Opens Linkedin homepage without login in
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/')

# Accepts cookie policy using xpath
time.sleep(2)
accCookie = driver.find_element(By.XPATH, '//button[contains(.,"Accept")]')
accCookie.click();

# 