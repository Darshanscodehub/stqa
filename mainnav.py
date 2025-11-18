from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. Initialize Chrome browser (with parentheses)
driver = webdriver.Chrome()

# 2. Open Google
driver.get("https://www.google.com/")
driver.get("https://monkeytype.com/")
driver.maximize_window()

driver.refresh()
input("Enter to Backward")
driver.back()
input("Enter to go foward")
driver.forward()

#Using Webelement Locator for XPATH
search_txtbox = driver.find_element(By.XPATH,"//textarea[@name='q']")
search_txtbox.send_keys('The Batman')
search_txtbox.send_keys(Keys.ENTER)

search_txtbox.send_keys('m')

input("hhh")