import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")

# locate dropdown
mydropdown = driver.find_element(By.ID, "dropdown")
dropdown = Select(mydropdown)

# select by visible text
dropdown.select_by_visible_text("Option 1")
time.sleep(2)
print(f"Selected option: {dropdown.first_selected_option.text}")

# select by value
dropdown.select_by_value("2")
time.sleep(2)
print(f"Selected option: {dropdown.first_selected_option.text}")

# select by index (2 → Option 2)
dropdown.select_by_index(2)
time.sleep(2)
print(f"Selected option: {dropdown.first_selected_option.text}")


