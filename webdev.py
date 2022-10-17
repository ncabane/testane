from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get('https://web.dev/measure/')

# Waits 1 second and then clicks OK button
time.sleep(1)
acceptCookie = driver.find_element(By.CSS_SELECTOR, '.web-snackbar__actions > .button:nth-child(2)')
acceptCookie.click();

# Clicks on URL bar, inserts my own paget
testUrl = driver.find_element(By.CSS_SELECTOR, '.lh-input')
testUrl.click();
testUrl.send_keys('https://nicolascabane.com')

# Runs the audit
runUrl = driver.find_element(By.ID,'run-lh-button')
runUrl.click();

# Waits for the result and clicks on View report
time.sleep(15)
viewRep = driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/web-lighthouse-viewer/div[1]/span[1]/a')
viewRep.click();
