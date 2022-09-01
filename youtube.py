from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get('https://www.youtube.com')

# Waits 2 seconds and then clicks OK button
time.sleep(2)
acceptCookie = driver.find_element(By.CSS_SELECTOR, '.ytd-consent-bump-v2-lightbox:nth-child(2) > .yt-simple-endpoint > #button')
acceptCookie.click();

# Searchs for my name on the search bar
time.sleep(2)
searchMe = driver.find_element(By.NAME, 'search_query')
searchMe.click();
searchMe.send_keys("Nicolas Cabane");

# Clicks the search button
time.sleep(2)
searchBtn = driver.find_element(By.CSS_SELECTOR, '#search-icon-legacy')
searchBtn.click();

# Closes the browser
driver.close();

