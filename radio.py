from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Initialize Chrome browser
driver = webdriver.Chrome()

# 2. Open Facebook
driver.get("https://www.fb.com/")

# 3. Wait until "Create new account" button is clickable
wait = WebDriverWait(driver, 15)
create_new_account = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="open-registration-form-button"]'))
)

time.sleep(5)

# 4. Click the button
create_new_account.click()

time.sleep(10)  # Just to keep the window open so you can see the result
driver.quit()
