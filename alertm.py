from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click button to trigger alert
driver.find_element("xpath", "//button[text()='Click for JS Alert']").click()
time.sleep(3)

# Switch to alert
alert = driver.switch_to.alert
print("Alert text:", alert.text)

# Accept the alert
alert.accept()

time.sleep(3)
driver.quit()
