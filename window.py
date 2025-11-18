from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
wait = WebDriverWait(driver,10)

original_window = driver.current_window_handle

driver.switch_to.new_window('window')
wait.until(EC.number_of_windows_to_be(2))

driver.execute_script("window.open('https://www.google.com/')")
wait.until(EC.number_of_windows_to_be(3))

all_windows = driver.window_handles
for window in all_windows:
    if window != original_window:
        driver.switch_to.window(window)
        break

driver.quit()

#Homework: Try with two different drivers
