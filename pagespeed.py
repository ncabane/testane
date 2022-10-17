from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get('https://pagespeed.web.dev/')

# Waits 1 second and then clicks OK button
time.sleep(1)
acceptCookie = driver.find_element(By.XPATH, '//input[@id="i2"]')
acceptCookie.click();

# Clicks on URL bar, inserts my own paget
testUrl = driver.find_element(By.XPATH, '//*[@id="i2"]')
testUrl.click();
testUrl.send_keys('https://nicolascabane.com/')

# Runs the audit
runUrl = driver.find_element(By.CSS_SELECTOR, '.VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-RLmnJb')
runUrl.click();
