import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil

def get_webdriver_options():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    return options

def run_selenium_with_code(code):
    service = Service(executable_path=shutil.which('chromedriver'))
    options = get_webdriver_options()
    result = {"customer_details": "", "complaint": "", "error": ""}
    with webdriver.Chrome(service=service, options=options) as driver:
        try:
            driver.get("https://respond.bbb.org/respond/")
            
            # Assuming there's an input field for the code, adjust as necessary
            input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "code"))
            )
            input_field.send_keys(code)
            
            # Assuming there's a submit button, adjust as necessary
            submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_button.click()
            
            # Adjust the wait condition as necessary for your application's response
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".customer-details"))
            )
            
            # Scrape the customer details and complaint, adjust selectors as necessary
            result["customer_details"] = driver.find_element(By.CSS_SELECTOR, ".customer-details").text
            result["complaint"] = driver.find_element(By.CSS_SELECTOR, ".complaint-details").text
            
        except Exception as e:
            result["error"] = str(e)
    
    return result

# Streamlit UI
st.title("BBB Complaint Details Scraper")

code = st.text_input("Enter Code", "")

if st.button("Fetch Complaint Details"):
    if code:
        result = run_selenium_with_code(code)
        if result["error"]:
            st.error("Failed to fetch details: " + result["error"])
        else:
            st.success("Details fetched successfully!")
            st.subheader("Customer Details:")
            st.write(result["customer_details"])
            st.subheader("Complaint:")
            st.write(result["complaint"])
    else:
        st.error("Please enter a code.")
