from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil
import time  # For simplicity in waiting (consider using WebDriverWait for production code)

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
    result = {}
    
    with webdriver.Chrome(service=service, options=options) as driver:
        driver.get("https://respond.bbb.org/respond/")  # Navigate to the login page
        
        # Assuming 'code' is the identifier for the input field for entering the access code
        input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cd")))
        input_field.send_keys(code)  # Enter the code
        
        submit_button = driver.find_element(By.NAME, "btn")  # Assuming 'btn' is the submit button name
        submit_button.click()  # Click the submit button to log in
        
        # Wait for the page with the iframe to load (adjust the condition as necessary)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe_selector")))  # Adjust the selector for the iframe
        
        # Switch to the iframe to interact with its content
        # driver.switch_to.frame("iframe_id_or_name")  # Uncomment and adjust if the iframe has an id or name
        
        # Extract the required details
        time.sleep(5)  # Simplistic wait; use WebDriverWait for better reliability
        result["sent_date"] = driver.find_element(By.ID, "cp1_mv1_lblSent").text
        result["from"] = driver.find_element(By.ID, "cp1_mv1_lblFrom").text
        result["to"] = driver.find_element(By.CSS_SELECTOR, "div.fld").text  # This might need adjustment
        result["subject"] = driver.find_element(By.ID, "cp1_mv1_lblSubject").text
        result["message_body"] = driver.find_element(By.ID, "section-to-print").text

        return result

# Example usage
if __name__ == "__main__":
    import streamlit as st

    st.title("BBB Complaint Details Scraper")

    code = st.text_input("Enter Code", "")

    if st.button("Fetch Complaint Details"):
        if code:
            result = run_selenium_with_code(code)
            if "error" in result:
                st.error("Failed to fetch details: " + result["error"])
            else:
                st.success("Details fetched successfully!")
                st.subheader("Sent Date:")
                st.write(result["sent_date"])
                st.subheader("From:")
                st.write(result["from"])
                st.subheader("To:")
                st.write(result["to"])
                st.subheader("Subject:")
                st.write(result["subject"])
                st.subheader("Message Body:")
                st.write(result["message_body"])
        else:
            st.error("Please enter a code.")
