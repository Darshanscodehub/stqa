from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

driver.save_screenshot('arnav.png') #Takes a full page screenshot and saves in root

google_logo = driver.find_element(By.XPATH,"//div[@class='k1zIA rSk4se']//*[name()='svg']")
google_logo.screenshot("img_logo.png")

driver.maximize_window()  # Maximizes the current window
time.sleep(3)

driver.minimize_window()  # Minimizes the current window
time.sleep(3)

driver.fullscreen_window()  # Sets the current window to fullscreen
time.sleep(3)

# Get current window position
window_position = driver.get_window_position()
print("Window Position: ", window_position)

# Set window position
driver.set_window_position(200, 100)
time.sleep(3)

# Get current window size
window_size = driver.get_window_size()
print("Window Size: ", window_size)

# Set window size
driver.set_window_size(1024, 768)
time.sleep(3)

driver.quit()
