import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Open Facebook in the first window
driver.get("https://www.facebook.com")
print("Opened Facebook")
time.sleep(3)

# Store the original window handle
original_window = driver.current_window_handle
print(">>> Original window handle:", original_window, type(original_window))

# Open a new browser window
driver.switch_to.new_window('window')
wait.until(EC.number_of_windows_to_be(2))
print("Opened a new blank window")
time.sleep(3)

# Open Google in a new tab using JavaScript
driver.execute_script("window.open('https://www.google.com/')")
wait.until(EC.number_of_windows_to_be(3))
print("Opened Google in a new tab")
time.sleep(3)

# Get all window handles
all_windows = driver.window_handles
print(">>> All window handles:", all_windows, type(all_windows))

# Switch to the first non-original window
for window in all_windows:
    if window != original_window:
        driver.switch_to.window(window)
        print("Switched to window/tab:", driver.title)
        time.sleep(3)
        break

# Keep everything open for a bit
print("Pausing for you to observe the windows...")
time.sleep(10)

# Close all windows and quit session
driver.quit()
print("Closed all windows and ended session")
