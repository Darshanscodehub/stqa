from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. Initialize Chrome browser (with parentheses)
driver = webdriver.Chrome()

# 2. Open Google
driver.get("https://www.google.com/")

single_search_txtbox = driver.find_element(By.XPATH,"//textarea")

multi_search_txtbox = driver.find_elements(By.XPATH,"//textarea")

# print(type(single_search_txtbox))
# print(type(multi_search_txtbox))

# Output:
# DevTools listening on ws://127.0.0.1:51218/devtools/browser/d05b8d81-db8b-4ecb-8230-c0cd86082b19
# <class 'selenium.webdriver.remote.webelement.WebElement'>
# <class 'list'>

# print("first: ", single_search_txtbox)
# print("second: ", multi_search_txtbox)

multi_search_txtbox.send_keys('The Batman')
multi_search_txtbox.send_keys(Keys.ENTER)

input("Enter something to end program: ")

# Output:
# py main2.py

# DevTools listening on ws://127.0.0.1:60471/devtools/browser/a5d4f296-8352-4593-bcbc-c6efdd072ca3
# Traceback (most recent call last):
#   File "D:\Selenium\main2.py", line 26, in <module>
#     multi_search_txtbox.send_keys('The Batman')
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'list' object has no attribute 'send_keys'
