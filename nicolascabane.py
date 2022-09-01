from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get('https://nicolascabane.com')

# Clicks hamburger menu
clickMenu = driver.find_element(By.CSS_SELECTOR, '.navbar-toggler-icon')
clickMenu.click();

# Clicks CV
clickCv = driver.find_element(By.LINK_TEXT, 'CV')
clickCv.click();

# Clicks SERVICIOS
clickMenu.click();
clickServ = driver.find_element(By.LINK_TEXT, 'SERVICIOS')
clickServ.click();






