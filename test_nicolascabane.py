from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get('https://nicolascabane.com')

# Clicks hamburger menu
clickMenu = driver.find_element(By.CSS_SELECTOR, '.navbar-toggler-icon')
clickMenu.click();

# Waits 2 seconds
time.sleep(2)

# Clicks CV
clickCv = driver.find_element(By.LINK_TEXT, 'CV')
clickCv.click();

# Waits 2 seconds
time.sleep(2)

# Clicks hamburger menu
clickMenu = driver.find_element(By.CSS_SELECTOR, '.navbar-toggler-icon')
clickMenu.click();

# Waits 2 seconds
time.sleep(2)

# Clicks SERVICIOS
clickServ = driver.find_element(By.LINK_TEXT, 'SERVICIOS')
clickServ.click();

# Waits 2 seconds
time.sleep(2)

# Clicks hamburger menu
clickMenu = driver.find_element(By.CSS_SELECTOR, '.navbar-toggler-icon')
clickMenu.click();

# Waits 2 seconds
time.sleep(2)

# Clicks SOBRE MI
clickServ = driver.find_element(By.LINK_TEXT, 'SOBRE MI')
clickServ.click();

# Waits 2 seconds
time.sleep(2)

# Clicks hamburger menu
clickMenu = driver.find_element(By.CSS_SELECTOR, '.navbar-toggler-icon')
clickMenu.click();

# Waits 2 seconds
time.sleep(2)

# Clicks CONTACTO
clickServ = driver.find_element(By.LINK_TEXT, 'CONTACTO')
clickServ.click();

# Goes back to home page
time.sleep(2)
backHome = driver.find_element(By.CSS_SELECTOR, '.site-title')
backHome.click();

# Fills form name
time.sleep(2)
formName = driver.find_element(By.ID, 'wpforms-52-field_0')
formName.send_keys("Juana")

# Fills form last name
formLast = driver.find_element(By.ID, 'wpforms-52-field_0-last')
formLast.send_keys("Manso")

# Fills email field
formEmail = driver.find_element(By.ID, 'wpforms-52-field_1')
formEmail.send_keys("juanamanso@juanamanso.com")

# Check one checkbox
checkThat = driver.find_element(By.ID, 'wpforms-52-field_4_1')
checkThat.click();

# Press send button
sendBtn = driver.find_element(By.ID, 'wpforms-submit-52')
sendBtn.click();
time.sleep(4)

# Generates a HTML report
def test_SeleniumTest():
    print("Report")

# Closes the browser
driver.close()