from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/nested_frames")

# ---- TOP → LEFT ----
driver.switch_to.frame("frame-top")   # switch to top frame
print("Switched to top frame")

driver.switch_to.frame("frame-left")  # inside left frame
print("Switched to left frame")
left_frame = driver.find_element(By.TAG_NAME, "body")
print("Left Frame Text:", left_frame.text)

driver.switch_to.parent_frame()       # back to top
print("Back to top frame")

# ---- TOP → MIDDLE ----
driver.switch_to.frame("frame-middle")
print("Switched to middle frame")
middle_frame = driver.find_element(By.ID, "content")
print("Middle Frame Text:", middle_frame.text)

driver.switch_to.parent_frame()       # back to top
print("Back to top frame")

# ---- TOP → RIGHT ----
driver.switch_to.frame("frame-right")
print("Switched to right frame")
right_frame = driver.find_element(By.TAG_NAME, "body")
print("Right Frame Text:", right_frame.text)

# Back to root (default content)
driver.switch_to.default_content()
print("Back to main document")

# ---- BOTTOM ----
driver.switch_to.frame("frame-bottom")
print("Switched to bottom frame")
bottom_frame = driver.find_element(By.TAG_NAME, "body")
print("Bottom Frame Text:", bottom_frame.text)

time.sleep(5)
driver.quit()
