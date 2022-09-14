from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

# Opens Taalhuis Amsterdam website
driver = webdriver.Chrome()
driver.get('https://taalhuisamsterdam.nl/')

# Accepts cookie overlay
time.sleep(2)
accCook = driver.find_element(By.CSS_SELECTOR, '.cookie-warning__accept')
accCook.click();

# Clicks on Courses
time.sleep(2)
clkCour = driver.find_element(By.CSS_SELECTOR, '.menu-item:nth-child(1) > .nav_hassubmenu')
clkCour.click();

# Clicks on Dutch
time.sleep(2)
clkDutch = driver.find_element(By.CSS_SELECTOR, '.adults .course-item:nth-child(1)')
clkDutch.click();

# Clicks on A1.1 course
time.sleep(2)
clka1 = driver.find_element(By.LINK_TEXT, 'A1.1')
clka1.click();

# Clicks on Go Back
time.sleep(2)
clkGoback = driver.find_element(By.CSS_SELECTOR, '.backlink--header')
clkGoback.click();

# Closes the browser
driver.close();