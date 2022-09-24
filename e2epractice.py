from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

# Opens Linkedin homepage without login in
driver = webdriver.Chrome()
driver.get('http://automationpractice.com/index.php/')
