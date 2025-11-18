from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

confirm_button = driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']")
confirm_button.click()
time.sleep(3)

alert = driver.switch_to.alert

print("Alert text: ", alert.text)
alert.accept()

result = driver.find_element(By.ID,"result")
print("Page result after accepting alert: ", result.text)
time.sleep(3)


driver.quit()