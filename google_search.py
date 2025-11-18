from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Launch Chrome browser
driver = webdriver.Chrome()

try:
    # Open YouTube homepage
    driver.get("https://www.youtube.com/")

    # Wait for the search box to appear and enter the video title
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search_box.send_keys("Python tutorial for beginners")
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video-title"))
    )

    # Find and click the first video
    first_video = driver.find_element(By.ID, "video-title")
    first_video.click()

    # Let the video play for 10 seconds
    time.sleep(10)

except TimeoutException:
    print("Error: Timeout while waiting for elements to load.")
except NoSuchElementException:
    print("Error: One or more elements not found on the page.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
finally:
    # Close the browser
    driver.quit()
