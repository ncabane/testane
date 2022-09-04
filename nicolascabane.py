from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get('https://nicolascabane.com')

# Clicks hamburger menu
clickMenu = driver.find_element(By.CSS_SELECTOR, '.navbar-toggler-icon')
clickMenu.click();

# Waits 3 seconds
time.sleep(3)

# Clicks CV
clickCv = driver.find_element(By.LINK_TEXT, 'CV')
clickCv.click();

# Waits 3 seconds
time.sleep(3)

# Clicks hamburger menu
clickMenu = driver.find_element(By.CSS_SELECTOR, '.navbar-toggler-icon')
clickMenu.click();

# Waits 3 seconds
time.sleep(3)

# Clicks SERVICIOS
clickServ = driver.find_element(By.LINK_TEXT, 'SERVICIOS')
clickServ.click();

# Waits 3 seconds
time.sleep(3)

# Clicks hamburger menu
clickMenu = driver.find_element(By.CSS_SELECTOR, '.navbar-toggler-icon')
clickMenu.click();

# Waits 3 seconds
time.sleep(3)

# Clicks SOBRE MI
clickServ = driver.find_element(By.LINK_TEXT, 'SOBRE MI')
clickServ.click();

# Waits 3 seconds
time.sleep(3)

# Clicks hamburger menu
clickMenu = driver.find_element(By.CSS_SELECTOR, '.navbar-toggler-icon')
clickMenu.click();

# Waits 3 seconds
time.sleep(3)

# Clicks CONTACTO
clickServ = driver.find_element(By.LINK_TEXT, 'CONTACTO')
clickServ.click();