import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

def initialize_driver():
    try:
        # Set up Chrome WebDriver with options
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Optional, for headless operation
        
        # Initialize Chrome WebDriver using ChromeDriverManager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    except Exception as e:
        st.error(f"Error initializing WebDriver: {str(e)}")
        return None

def run_selenium_script(customer_name):
    # Temporarily hardcoded for testing purposes
    username = "rwallace@lendcare.ca"
    # Retrieve the password securely from Streamlit secrets
    password = "Fuckoffboo123@!@!"
    
    # Initialize the WebDriver
    driver = initialize_driver()
    if driver is None:
        return
    
    try:
        driver.get("https://www.bbb.org/kitchener/login")
        
        # Use explicit waits instead of fixed sleeps
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(username)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Log In')]"))).click()

        # Navigate and perform actions
        # Example of navigating with explicit wait for URL change
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

        # Placeholder for further actions...

        return "Success - Actions completed"
    except NoSuchElementException as e:
        return f"Element not found error: {str(e)}"
    except TimeoutException as e:
        return f"Timeout error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    finally:
        # Quit the WebDriver session to release resources
        if driver is not None:
            driver.quit()

# Streamlit UI setup
st.title('Automated Web Interaction with Selenium')

customer_name = st.text_input("Enter Customer Name", "")

if st.button("Run Automation"):
    if customer_name:
        result = run_selenium_script(customer_name)
        st.success(result)
    else:
        st.error("Please enter a customer name.")
