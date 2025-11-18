from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. Initialize Chrome browser
driver = webdriver.Chrome()

# 2. Open Google
driver.get("https://www.google.com/")

# Find single and multiple textareas
single_search_txtbox = driver.find_element(By.XPATH, "//textarea")
multi_search_txtbox = driver.find_elements(By.XPATH, "//textarea")

# Use the first element from the list
search_box = multi_search_txtbox[0]

# Type search text and press Enter
search_box.send_keys("The Batman")
search_box.send_keys(Keys.ENTER)

input("Enter something to end program: ")
