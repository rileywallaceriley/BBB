import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Streamlit UI setup
st.title('BBB Complaint Details Scraper')

code = st.text_input("Enter Code", "")

if st.button("Scrape Details"):
    if code:
        # Function to run the Selenium script
        def scrape_complaint_details(code):
            try:
                options = Options()
                options.add_argument("--headless")  # For headless operation
                driver = webdriver.Chrome(options=options)

                driver.get("https://respond.bbb.org/respond/")

                # Assume 'input_code' is the name of the input field for the code, adjust as necessary
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "input_code"))
                ).send_keys(code)

                # Assume this is the way to submit the code, adjust selector as needed
                submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
                submit_button.click()

                # Wait for the pop-up or new page to load
                # This condition might need to be adjusted based on the actual page behavior
                WebDriverWait(driver, 10).until(EC.url_contains("complaints"))

                # Scrape customer details and the complaint
                # Adjust the selectors based on the actual content structure
                customer_details = driver.find_element(By.ID, "customer_details").text
                complaint = driver.find_element(By.ID, "complaint_text").text

                return {"customer_details": customer_details, "complaint": complaint}
            except Exception as e:
                return f"An error occurred: {str(e)}"
            finally:
                if 'driver' in locals():
                    driver.quit()

        # Running the scraping function
        result = scrape_complaint_details(code)

        if isinstance(result, dict):
            st.success("Scraping successful!")
            st.write("Customer Details:", result["customer_details"])
            st.write("Complaint:", result["complaint"])
        else:
            st.error(result)
    else:
        st.error("Please enter a code.")
