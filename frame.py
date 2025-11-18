from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

# Switch into iframe
driver.switch_to.frame("mce_0_ifr")
print("Switched to iframe")

iframe_body = driver.find_element(By.TAG_NAME, "body")
iframe_body.send_keys("India")

time.sleep(5)

driver.switch_to.default_content()

main_header = driver.find_element(By.TAG_NAME, "h3")
print("Main Document Header: ", main_header.text)

time.sleep(5)

driver.quit()