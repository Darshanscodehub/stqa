"""
This script automates the process of opening Facebook, 
clicking the 'Create new account' button, and filling out 
the sign-up form using Selenium WebDriver in Python.

Steps performed:
1. Launches Chrome browser and navigates to Facebook.
2. Waits until the 'Create new account' button is clickable and clicks it.
3. Fills out the registration form fields:
   - First name
   - Surname
   - Mobile number or email
   - Password
   - Date of birth (day, month, year)
   - Gender (Male in this example)
4. Submits the form by clicking the 'Sign Up' button.
5. Waits for 10 seconds before closing the browser.

Note:
- Dummy data is used for demonstration purposes.
- Some fields (like 'Re-enter email') may appear dynamically 
  and should be handled with explicit waits if needed.
- This script is for practice/learning only; 
  Facebook may block automated sign-ups using real information.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.fb.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 15)

# Step 1: Click "Create new account"
create_new_account = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="open-registration-form-button"]'))
)
create_new_account.click()

# Step 2: Fill form fields
first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
first_name.send_keys("Arnav")

last_name = driver.find_element(By.NAME, "lastname")
last_name.send_keys("Chandure")

email = driver.find_element(By.NAME, "reg_email__")
email.send_keys("arnav123@example.com")

password = driver.find_element(By.NAME, "reg_passwd__")
password.send_keys("StrongPassword123")

# Step 3: Select date of birth
Select(driver.find_element(By.NAME, "birthday_day")).select_by_visible_text("16")
Select(driver.find_element(By.NAME, "birthday_month")).select_by_visible_text("Sep")
Select(driver.find_element(By.NAME, "birthday_year")).select_by_visible_text("2000")

# Step 4: Select gender (Male)
gender = driver.find_element(By.XPATH, '//input[@name="sex" and @value="2"]')
gender.click()

# Step 5: Click Sign Up
signup_btn = driver.find_element(By.NAME, "websubmit")
signup_btn.click()

time.sleep(10)
driver.quit()
