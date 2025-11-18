from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/nested_frames")

driver.switch_to.frame("frame-top") #Switch to top frame (main frame)
print("Switch to top frame")

driver.switch_to.frame("frame-left") #Switch to left frame within top frame
print("Switch to left frame")

left_frame = driver.find_element(By.TAG_NAME, "body")
print("Left Frame Text: ", left_frame.text) #get text from the left frame

driver.switch_to.parent_frame()#Switch back to the top frame
print("Switched back to top frame")

driver.switch_to.frame("frame-middle") #Switch to middle frame within top frame
print("Switch to middle frame")

middle_frame = driver.find_element(By.TAG_NAME, "body")
print("Middle Frame Text: ", middle_frame.text) #get text from the middle frame

driver.switch_to.parent_frame()#Switch back to the top frame
print("Switched back to top frame")

driver.switch_to.default_content()

driver.switch_to.frame("frame-bottom") #Now switch to bottom frame
bottom_frame = driver.find_element(By.TAG_NAME, "body")
print("Bottom Frame Text: ", bottom_frame.text) # Get text from bottom frame

driver.quit()

