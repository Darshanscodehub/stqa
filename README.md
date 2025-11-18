4+14 marks Question

Write a detailed test plan in IEEE test plan format for an application which will allow users to enroll for a MOOC (Massive Open Online Course) through a registration process. On the home page. users can find Upcoming courses, last submitted or Updated courses. Users can also browse by Course categories and attend the same free of charge. Payment for MOOC course materials can be done in net-banking or card payment mode.	MARKS: 14	 
 									 
QUESTION 2: TEST CASE	 
Write min 12 test cases for above case study	MARKS: 06	 


ANSWER 1: TEST PLAN
Sr. No.	Test Plan Point	Answer
1	Test Plan Identifier	MOOC_APP_TESTPLAN_V1.0
2	References	IEEE std 829-1998 Test Documentation Standard
3	Introduction	This Test Plan describes the strategy, scope, objectives, and schedule for testing the MOOC Application. The purpose of this application is to allow users to register, browse, and enroll in online courses, view upcoming and updated courses, and make payments for paid materials using net-banking or card mode.
4	Features to be Tested	• User Registration and Login
• Course Browsing by Categories
• Viewing Upcoming and Updated Courses
• Enrollment in Free and Paid Courses
• Payment Gateway (Net-Banking, Card Payment)
• Confirmation Email/SMS after Enrollment
5	Approach	Functional, Usability, and Security Testing will be performed. Manual testing will be conducted for UI verification. Selenium will be used for automation. Payment gateway testing will include validation and error handling.
6	Environmental Needs	Hardware: Windows 10/11, 8GB RAM
Software: Chrome, MySQL, XAMPP
Environment: Staging Server replicating production setup.
7	Staffing & Training Needs	QA Team: Test Manager, Test Engineers, Automation Tester
Training: Selenium, JIRA, Payment Testing.
8	Responsibilities	Test Manager: Approve plan
QA Engineers: Execute tests and report bugs
Developers: Fix issues
Client: Validate final results
9	Schedule	Test Planning: 01/03/2025 – 05/03/2025
Test Design: 06/03/2025 – 10/03/2025
Test Execution: 11/03/2025 – 20/03/2025
Defect Retesting: 21/03/2025 – 25/03/2025
Sign-off: 26/03/2025
10	Approval	Prepared By: QA Team
Reviewed By: Test Manager
Approved By: Project Manager


ANSWER 2: TEST CASES
Project Name: MOOC Application	Module Name: Enrollment & Payment	Date Created: 01/03/2025
Tester Name: QA Engineer	Manager Name: Test Manager	Date Reviewed: 05/03/2025
Reviewed By: QA Lead	Test Data: User Credentials, Course Info, Payment Details
Sr. No.	Test Case ID	Test Scenario / Step	Test Data	Expected Result	Actual Result	Pass / Fail
1	TC001	Verify registration with valid details	Valid name, email, password	User registered successfully		
2	TC002	Verify registration with invalid email	abc@xyz	Error message displayed		
3	TC003	Verify login with valid credentials	Valid email, password	Redirected to dashboard		
4	TC004	Verify login with invalid password	Valid email, wrong password	Error: Invalid credentials		
5	TC005	Verify browsing courses by category	Select 'Computer Science'	Courses displayed for category		
6	TC006	Verify Upcoming Courses section	N/A	Upcoming course list displayed		
7	TC007	Verify enrolling in a free course	Click Enroll on free course	Enrolled successfully		
8	TC008	Verify payment via Net Banking	Valid bank details	Payment success confirmation		
9	TC009	Verify payment via Card Payment	Valid card number, CVV	Payment success confirmation		
10	TC010	Verify confirmation email after payment	Registered email ID	Email received with details		
11	TC011	Verify Updated Courses section	Admin updates course	Updated course visible		
12	TC012	Verify logout functionality	Click Logout	User redirected to login page		



### **Question 2: Automate Google Search**

Write a Python program using **Selenium WebDriver** to automate a Google search.

Your program should:

1. Launch the Chrome browser and open **[https://www.google.com/](https://www.google.com/)**.
2. Enter a search query (e.g., `"Top 10 programming languages 2025"`) into the search bar.
3. Click the **Google Search** button (or press Enter).
4. Wait for the results page to load and print the titles of the **first 5 search results** in the console.
5. Close the browser after completion.

**Note:**

* Use **explicit waits** to ensure the search bar and results are loaded.
* Avoid using `time.sleep()` for synchronization — use `WebDriverWait`.

Answer:-
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
    # Open Google homepage
    driver.get("https://www.google.com/")

    # Wait for the search box to appear and enter the query
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Top 10 programming languages 2025")
    search_box.send_keys(Keys.RETURN)

    # Wait for the results page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'h3'))
    )

    # Find the first 5 search result titles
    results = driver.find_elements(By.CSS_SELECTOR, 'h3')

    print("First 5 Google search results:")
    for i in range(min(5, len(results))):
        title = results[i].text.strip()
        if title:  # Only print non-empty results
            print(f"{i+1}. {title}")

except TimeoutException:
    print("Error: Timeout while waiting for elements to load.")
except NoSuchElementException:
    print("Error: One or more elements not found on the page.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
finally:
    time.sleep(2)
    driver.quit()


### **Question 3: Automate LinkedIn Login**

Write a Python script using **Selenium WebDriver** to automate the LinkedIn login process.

Your program should:

1. Open **[https://www.linkedin.com/login](https://www.linkedin.com/login)** in Chrome.
2. Enter a sample username (email) and password into the respective fields.
3. Click the **“Sign in”** button.
4. Capture and print the **page title** after login attempt.
5. Close the browser.

Answer:-
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
    # Open LinkedIn login page
    driver.get("https://www.linkedin.com/login")

    # Wait for the username field to appear and enter the email
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("test@example.com")  # Dummy email

    # Enter dummy password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("testpass")  # Dummy password

    # Click the Sign in button
    sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    sign_in_button.click()

    # Wait for the page to load after login attempt
    time.sleep(5)  # Adjust as needed

    # Capture and print the page title
    page_title = driver.title
    print(f"Page title after login attempt: {page_title}")

except TimeoutException:
    print("Error: Timeout while waiting for elements to load.")
except NoSuchElementException:
    print("Error: One or more elements not found on the page.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
finally:
    time.sleep(2)
    driver.quit()


### **Question 4: Automate YouTube Video Search**

Write a Python program using **Selenium WebDriver** to search for a video on YouTube.

Your program should:

1. Launch the Chrome browser and open **[https://www.youtube.com/](https://www.youtube.com/)**.
2. Enter a video title (e.g., “Python tutorial for beginners”) into the search bar.
3. Click the **Search** button.
4. Wait for results to appear, then click on the **first video** from the list.
5. Let the video play for 10 seconds before closing the browser.

**Note:**

* Use **explicit waits** to wait for the search results.

Answer:-
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


Write a Python program using **Selenium WebDriver** to automate the process of creating a new Facebook account.

Your program should:

1. Launch the Chrome browser and open the Facebook website.
2. Click the **"Create new account"** button.
3. Fill in the sign-up form with the following details:

   * First name
   * Surname
   * Mobile number or email
   * Password
   * Date of birth (Day, Month, Year)
   * Gender (select Male)
4. Click the **"Sign Up"** button.
5. Wait for 10 seconds before closing the browser.

**Note:**

* Use **explicit waits** to ensure elements are clickable or visible before interacting with them.
* This program is for **practice purposes only** and should not be used for real account creation.

Answer:-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Launch Chrome browser
driver = webdriver.Chrome()

try:
    # Open Facebook website
    driver.get("https://www.facebook.com/")

    # Wait for and click the "Create new account" button
    create_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Create new account"))
    )
    create_account_button.click()

    # Wait for the sign-up form to appear (modal)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "firstname"))
    )

    # Fill in the first name
    first_name_field = driver.find_element(By.NAME, "firstname")
    first_name_field.send_keys("John")

    # Fill in the surname
    surname_field = driver.find_element(By.NAME, "lastname")
    surname_field.send_keys("Doe")

    # Fill in the mobile number or email
    email_field = driver.find_element(By.NAME, "reg_email__")
    email_field.send_keys("test@example.com")

    # Fill in the password
    password_field = driver.find_element(By.NAME, "reg_passwd__")
    password_field.send_keys("password123")

    # Select date of birth: Day
    day_select = Select(driver.find_element(By.NAME, "birthday_day"))
    day_select.select_by_value("1")

    # Select date of birth: Month
    month_select = Select(driver.find_element(By.NAME, "birthday_month"))
    month_select.select_by_value("1")

    # Select date of birth: Year
    year_select = Select(driver.find_element(By.NAME, "birthday_year"))
    year_select.select_by_value("1990")

    # Select gender: Male
    male_radio = driver.find_element(By.XPATH, "//input[@name='sex'][@value='2']")
    male_radio.click()

    # Click the "Sign Up" button
    sign_up_button = driver.find_element(By.NAME, "websubmit")
    sign_up_button.click()

    # Wait for 10 seconds before closing the browser
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






                                                                                                                                                Selenium Summary                                                                                                                                     -By Keshav Potdar
Level	Category	Command	Description
WebElement	Locator	driver.find_element(By.ID, '<id>')	Find WebElement by ID
WebElement	Locator	driver.find_element(By.NAME, '<name>')	Find WebElement by Name
WebElement	Locator	driver.find_element(By.CLASS_NAME, '<cls>')	Find WebElement by Class
WebElement	Locator	driver.find_element(By.TAG_NAME, '<tag>')	Find WebElement by Tag
WebElement	Locator	driver.find_element(By.LINK_TEXT, '<text>')	Find WebElement by Link Text
WebElement	Locator	driver.find_element(By.PARTIAL_LINK_TEXT, '<txt>')	Find WebElement by Partial Link
WebElement	Locator	driver.find_element(By.XPATH, '<//div>')	Find WebElement by XPath
WebElement	Locator	driver.find_element(By.CSS_SELECTOR, '<div.cls>')	Find WebElement by CSS
WebElement	Locator	driver.find_elements(By.XPATH, '<//div>')	Find multiple WebElements
WebElement	Locator-XPath	//div[@id='<value>']	Find WebElement by attribute
WebElement	Locator-XPath	//div[contains(@class, '<btn>')]	XPath contains() example
WebElement	Locator-XPath	//div[contains(text(), '<msg>')]	XPath contains() example
WebElement	Locator-XPath	//div[text()='<Submit>']	XPath by text() example
WebElement	Locator-XPath	//div[starts-with(@id, '<You are>') and @type='msg']	XPath starts-with() example
WebElement	Action	element.click()	Click element
WebElement	Action	element.send_keys('<keshav>')	Enter text
WebElement	Action	element.clear()	Clear input
WebElement	Action	element.submit()	Submit form
WebElement	Property	element.text	Get element text
WebElement	Property	element.get_attribute('<val>')	Get attribute value
WebElement	Property	element.get_dom_attribute('<id>')	Get DOM attribute
WebElement	Property	element.get_property('<checked>')	Get property
WebElement	Property	element.tag_name	Get tag name
WebElement	Property	element.size	Get size
WebElement	Property	element.location element.size element.rect	1.	Returns only position (x, y). Eg. {'x': 50, 'y': 120}
2.	Returns only dimensions (height, width). Eg. {'height': 100, 'width': 200}
3.	Returns both position, dimensions. Eg. {'height': 100, 'width': 200, 'x': 50, 'y': 120}
WebElement	Property	element.screenshot('<elem.png>')	Screenshot element
WebElement	State	element.is_displayed()	Check if visible
WebElement	State	element.is_enabled()	Check if enabled
WebElement	State	element.is_selected()	Check if selected
WebElement	ActionChains	ActionChains(driver).move_to_element(<WebEle>).click().perform()	Hover + click
WebElement	ActionChains	ActionChains(driver).double_click(<WebEle>).perform()	Double click
WebElement	ActionChains	ActionChains(driver).context_click(<WebEle>).perform()	Right click
WebElement	ActionChains	ActionChains(driver).drag_and_drop(<SrcWebEle>, <DstWebEle>).perform()	Drag & drop
WebElement	Select	from selenium.webdriver.support.ui import Select
Select(<WebEle>).de/select_by_index(2)	De/Select by index
WebElement	Select	Select(<WebEle>).de/select_by_value('<India>')	De/Select by value
WebElement	Select	Select(<WebEle>).de/select_by_visible_text('<India>')	De/Select by text
WebElement	Select	Select(<WebEle>).deselect_all()	Deselect all options
WebElement	Select	Select(<WebEle>).options	List all options
WebElement	Select	Select(<WebEle>).all_selected_options	List selected options
Exception	Exception	NoSuchElementException	Occurs when element not found. Fix: Use explicit waits or correct locator.
Exception	Exception	TimeoutException	Wait timed out. Fix: Increase wait time, validate locator.
Exception	Exception	ElementNotInteractableException	Element not interactable. Fix: Ensure visible & enabled, use waits.
Exception	Exception	StaleElementReferenceException	Element is no longer attached to DOM. Fix: Re-find element after refresh.
Exception	Exception	NoSuchWindowException	Window not found. Fix: Switch to correct window handle.
Exception	Exception	NoSuchFrameException	Frame not found. Fix: Verify frame locator & switch correctly.
Exception	Exception	ElementClickInterceptedException	Click blocked by another element. Fix: Scroll into view, wait until clickable.
Exception	Exception	InvalidSelectorException	Locator syntax invalid. Fix: Correct XPath/CSS syntax.
Exception	Exception	WebDriverException	Generic driver failure. Fix: Ensure driver/browser compatibility.
Exception	Exception	SessionNotCreatedException	Driver session failed. Fix: Update WebDriver & browser version.

                                                                                                                                                Selenium Summary                                                                                                                                     -By Keshav Potdar
Level	Category	Command	Description
Driver	Browser	driver.get('https://google.com')	Open a URL
Driver	Browser	driver.current_url	Get current URL
Driver	Browser	driver.title	Get page title
Driver	Browser	driver.page_source	Get page source HTML
Driver	Browser	driver.close()	Close current tab/window
Driver	Browser	driver.quit()	Quit browser & end session
Driver	Browser	driver.refresh() driver.forward() driver.back()	Refresh page
Navigate forward
Navigate back
Driver	Window	driver.current_window_handle	Get current window handle
Driver	Window	driver.window_handles	Get all window handles
Driver	Window	driver.switch_to.window(handle)	Switch to given window/tab
Driver	Window	driver.switch_to.new_window('tab') driver.switch_to.new_window('window')	Open new tab
Open new window
Driver	Window	driver.fullscreen_window()	Fullscreen mode
Driver	Window	driver.maximize_window()	Maximize window
Driver	Window	driver.minimize_window()	Minimize window
Driver	Window	driver.set_window_size(1024,768)	Set custom size
Driver	Window	driver.get_window_size()	Get window size
Driver	Window	driver.get_window_position()	Get window position
Driver	Window	driver.set_window_position(200,100)	Move window position
Driver	Alert	alert = driver.switch_to.alert	Switch to active alert
Driver	Alert	alert.accept()	Accept alert
Driver	Alert	alert.dismiss()	Dismiss alert
Driver	Alert	alert.send_keys('Keshav')	Enter text in prompt
Driver	Alert	alert.text	Get alert text
Driver	Frame	driver.switch_to.frame('frame_name')	Switch by name
Driver	Frame	driver.switch_to.frame(0)	Switch by index
Driver	Frame	driver.switch_to.frame(<WebEle>)	Switch by WebElement
Driver	Frame	driver.switch_to.parent_frame()	Switch to parent
Driver	Frame	driver.switch_to.default_content()	Exit to main content
Driver	JavaScript	driver.execute_script('return document.title;')	Execute JS sync
Driver	JavaScript	driver.execute_async_script('callback();')	Execute JS async
Driver	Screenshot	driver.save_screenshot('page.png')	Full page screenshot
Driver	Cookies	driver.get_cookies()	Get all cookies
Driver	Cookies	driver.get_cookie('name')	Get single cookie
Driver	Cookies	driver.add_cookie({'name':'k','value':'v'})	Add cookie
Driver	Cookies	driver.delete_cookie('<sess_id>')	Delete one cookie
Driver	Cookies	driver.delete_all_cookies()	Delete all cookies
Driver	Logging	driver.get_log("browser") driver.get_log("performance")	browser : Fetches JavaScript console logs (e.g., warnings, errors)
performance: Captures browser performance logs (network, rendering, events)
Driver	Tool	driver.execute_cdp_cmd("Page.setDownloadBehavior",
        {"behavior": "allow",     "downloadPath": "/<path>"})	File downloads with DevTools (no prompt)
Driver	Tool	driver.set_network_conditions(
    offline=False,
    latency=100,                               # milliseconds     download_throughput=1024,   # bytes/second     upload_throughput=1024         # bytes/second
)	Test slow/unstable networks.
set_network_conditions() is wrapper on execute_cdp_cmd() with limited operations.
Driver	Tool	driver.install_addon("</path/to/extension.xpi>", temporary=<True>)	Install browser add-on (Firefox only)
Driver	Capabilities	from selenium.webdriver.chrome.options import Options
Options().add_argument('--headless')	Set Chrome option. Below are few more useful arguments like --headless:
--incognito                                       --ignore-certificate-errors
--start-maximized                           --disable-popup-blocking
--window-size=1920,1080            --mute-audio
--disable-notifications                   --disable-extensions
--disable-infobars (useul for automation)
--kiosk   (full screen mode)
Driver	Capabilities	options.set_capability("acceptInsecureCerts", True) options.set_capability("browserName", "chrome") options.set_capability("browserVersion", "stable") options.set_capability("platformName", "ANY") options.set_capability("acceptSslCerts", True)
options.set_capability("unhandledPromptBehavior", "dismiss") options.set_capability("strictFileInteractability", True)	# Accept SSL cert errors
# Browser type
# Specific version (or "latest"/"stable")
# OS platform ("WINDOWS", "LINUX", "MAC", "ANY") # Accept SSL certificates
# Auto-dismiss JS alerts
# Strict file handling
Driver	Capabilities	webdriver.Chrome(options=options)	Launch browser with above passed options
Driver	Timeouts	driver.set_page_load_timeout(<sec>)	Page load timeout, not applicable for WebEle finding.
Applies for driver.get(url), .back() .forward()
Driver	Timeouts	driver.set_script_timeout(<sec>)	Wait time for JavaScript execution  when used driver.execute_async_script(). Not applicable to execute_script() which is synchronous.
Driver	Wait	driver.implicitly_wait(<sec>)	Set implicit wait. Applicable for all findElement() only
Driver	Wait	from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC WebDriverWait(     driver,     timeout=<sec>,
    poll_frequency=<max_attempt>,     ignored_exceptions=[NoSuchElementException, ElementNotInteractableException] ).until(EC.element_to_be_clickable((By.ID,'<WebEle>')))	Set Explicit / Fluent  wait
EC.presence_of_element_located EC.visibility_of_element_located
EC.element_located_to_be_selected
EC.text_to_be_present_in_element
EC.frame_to_be_available_and_switch_to_it
EC.alert_is_present
EC.invisibility_of_element_located EC.number_of_windows_to_be


