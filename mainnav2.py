from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://monkeytype.com/")
driver.maximize_window()

current_url = driver.current_url
print("Current page URL: ", current_url)

current_title = driver.title
print("Current page Title: ", current_title)

current_page_source = driver.page_source
print("Current Page Source: ", current_page_source)
