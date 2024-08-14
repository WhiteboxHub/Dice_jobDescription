from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time

def test_login():
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Optional: run in headless mode
    # chrome_options.add_argument("--headless")

    # Initialize the Chrome WebDriver with options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        # Open the login page
        driver.get("https://www.dice.com/dashboard/login")

        # Maximize the browser window
        driver.maximize_window()

        # Wait for the email input field to be present and interactable
        email_input = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Please enter your email"]'))
        )
        email_input.clear()
        email_input.send_keys("email")
        email_input.send_keys(Keys.RETURN)
        
        # Wait for the password input field to be present and interactable
        password_input = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Enter Password"]'))
        )
        password_input.clear()
        password_input.send_keys("password")
        password_input.send_keys(Keys.RETURN)

        # Wait for the search term input field to be present and interactable
        search_input = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Search Term"]'))
        )
        search_input.clear()
        search_input.send_keys("frontend developer")
        search_input.send_keys(Keys.RETURN)

        # Wait for the search location input field to be present and interactable
        location_input = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Search Location"]'))
        )
        location_input.clear()
        location_input.send_keys("united states")
        location_input.send_keys(Keys.RETURN)

        # Wait for the "Search Jobs" button to be present and interactable
        search_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="submitSearch-button"]'))
        )
        search_button.click()

        # Wait for elements with the class 'card-title-link normal' to be present
        elements = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-title-link.normal'))
        )


        # Click the first element
        elements[0].click()
        print("Clicked the first element.")

        # element = driver.find_element(By.XPATH, "//*[text()='Read Full Job Description']")

        # ActionChains(driver)\
        # .scroll_to_element(element)\
        # .perform()

        footer = driver.find_element(By.TAG_NAME, "footer")
        scroll_origin = ScrollOrigin.from_element(footer, 0, -50)
        ActionChains(driver)\
        .scroll_from_origin(scroll_origin, 0, 200)\
        .perform()



        
        print("Scrolled to the element.")

        

    finally:
        # Inform the user that the browser will remain open
        print("The browser window will remain open. Close it manually when you're done.")
        time.sleep(600)

        # Close the WebDriver manually if needed (uncomment if you want to close it automatically)
        # driver.quit()

if __name__ == "__main__":
    test_login()
