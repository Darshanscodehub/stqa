# difference between close() and quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Initialize Chrome browser (with parentheses)
driver = webdriver.Chrome()

# 2. Open Google
driver.get("https://www.google.com/")

driver.switch_to.new_window("window")
driver.get("https://www.facebook.com")

driver.switch_to.new_window("tab")
driver.get("http://www.youtube.com")
time.sleep(10)

#driver.close()#will close current browser window
driver.quit() #will close all window