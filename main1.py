from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. Initialize Chrome browser (with parentheses)
driver = webdriver.Chrome()

# 2. Open Google
driver.get("https://www.google.com/")

# 3. Print the page title
print("Page title:", driver.title)

# 4. Maximize window
driver.maximize_window()

# 5. Find element by ID (example: search box has ID 'APjFqb')
search_box = driver.find_element(By.ID, "APjFqb")
print("Search box element:", search_box)

#Using Webelement Locator for XPATH
search_txtbox = driver.find_element(By.XPATH,"//textarea[@name='q']")
search_txtbox.send_keys('The Batman')
search_txtbox.clear()
search_txtbox.send_keys(Keys.ENTER)

input("hhh")