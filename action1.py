from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.set_page_load_timeout(20)
driver.maximize_window()

driver.get("https://imcc.mespune.in/")
wait = WebDriverWait(driver, 15)
actions = ActionChains(driver)

header = wait.until(
    EC.presence_of_element_located((By.XPATH,"//h2[contains(normalize-space(.),'Prominent Recruiters')]"))
)
logos = wait.until(
    EC.presence_of_all_elements_located((By.XPATH,"//h2[contains(normalize-space(.),'Prominent Recruiters')]/following::img"))
)
print("Total logos found: ", len(logos))

if len(logos)>=3:
    third_logo = wait.until(EC.visibility_of(logos[2])) #index 2 => 3rd logo
    time.sleep(2)
    actions.click_and_hold(third_logo).move_by_offset(-100,0).release().perform()
    #alternatively:actions.drag_and_drop_by_offset(thrid_logo,-100,0).perform()

    print("Dragged 3rd logo 100px to the left.")
    time.sleep(2)
else:
    print("Less than 3 logos found")
driver.quit()