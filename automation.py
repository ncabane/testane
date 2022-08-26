from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get('https://www.zalando.nl/outlet-heren/?sale=true')

# Waits 3 seconds and then clicks OK button
time.sleep(3)
acceptCookie = driver.find_element(By.ID, 'uc-btn-accept-banner')
acceptCookie.click();

# Clicks Alle filteren
clickAllfilter = driver.find_element(By.CSS_SELECTOR, '.hPWzFB > .DJxzzA > .RYghuO > .RYghuO')
clickAllfilter.click();

# Clicks Sorteren
clicksSorteren = driver.find_element(By.CSS_SELECTOR, '.DJxzzA:nth-child(1) .piG9a1')
clicksSorteren.click();

#Clicks Aanbiedingen
clicksAanbiedingen = driver.find_element(By.CSS_SELECTOR, '.ISbUTm:nth-child(5) .UEJYaG')
clicksAanbiedingen.click();

#Selects a product


# Closes the current window
driver.close()
