from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/checkboxes")

checkbox1 = driver.find_element(By.XPATH,"//form[@id='checkboxes']/input[1]")
checkbox2 = driver.find_element(By.XPATH,"//form[@id='checkboxes']/input[2]")

time.sleep(5)
if not checkbox1.is_selected():
    checkbox1.click()
time.sleep(5)
if checkbox1.is_selected():
    checkbox1.click()
# time.sleep(5)
# checkbox2.click()
# time.sleep(5)
# checkbox2.click()
# time.sleep(5)