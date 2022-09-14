from locale import delocalize
from textwrap import fill
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()
driver.get('https://www.megekko.nl/')

# Waits 2 seconds and then clicks OK button
time.sleep(3)
acceptCookie = driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
acceptCookie.click();

# Clicks on categories
time.sleep(2)
catOpen = driver.find_element(By.ID, 'searchFieldInputField')
catOpen.click();
catOpen.send_keys("Nvidia")
catOpen.send_keys(Keys.ENTER);

# Places an item in the shop cart
time.sleep(2)
addCart = driver.find_element(By.CLASS_NAME, 'shopbutton')
addCart.click();

# Fills email field
time.sleep(2)
fillEmail = driver.find_element(By.ID, 'email')
fillEmail.click();
fillEmail.send_keys("testane@testane.com")

# Selects country Nederland
time.sleep(2)
seLand = driver.find_element(By.ID, 'land')
seLand.click();
time.sleep(2)
seLand.click();

# Selects country type of consumer
time.sleep(2)
seCnsmr = driver.find_element(By.ID, 'zakelijk')
seCnsmr.click();
time.sleep(2)
seCnsmr.click();

# Fills in first name
time.sleep(2)
fillname = driver.find_element(By.ID, 'voornaam')
fillname.click();
fillname.send_keys("Jan")

# Fill Last name
time.sleep(2)
fillLast = driver.find_element(By.ID, 'achternaam')
fillLast.send_keys('Testane')

# Fills post code
time.sleep(2)
postCode = driver.find_element(By.ID, 'postcode')
postCode.send_keys("1010AA")

# Fills house number
time.sleep(2)
huisNum = driver.find_element(By.ID, 'huisnummer')
huisNum.send_keys("11")

# Fills apartment number or letter
time.sleep(2)
aptNum = driver.find_element(By.ID, 'toevoeging')
aptNum.send_keys("A")

# Fills street name
time.sleep(2)
stName = driver.find_element(By.ID, "adres")
stName.send_keys("Testanekade")

# Fills city
time.sleep(2)
fillCity = driver.find_element(By.ID, 'plaats')
fillCity.send_keys("Amsterdam")

# Fills phone number
time.sleep(2)
phoneNmr = driver.find_element(By.ID,'telefoon')
phoneNmr.send_keys("06123456")

# Selects delivery date
time.sleep(2)
delDate = driver.find_element(By.ID, 'leverdatum')
delDate.click();
time.sleep(2)
delDate.click();

# Selects delivery or collection place
time.sleep(2)
delCol = driver.find_element(By.ID, 'wl_alt0')
delCol.click();
time.sleep(2)
delCol.click();

# Closes the browser
driver.close()
