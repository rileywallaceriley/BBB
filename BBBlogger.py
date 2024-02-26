import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def scrape_bbb_complaint_details(complaint_code):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the BBB Response Portal login page
        login_page_url = "https://respond.bbb.org/respond/"
        driver.get(login_page_url)

        # Fixed delay to wait for the page to load
        time.sleep(30)

        # Input the complaint code
        code_input = driver.find_element(By.ID, "cd")
        code_input.clear()
        code_input.send_keys(complaint_code)

        # Submit the form
        submit_button = driver.find_element(By.ID, "btn")
        submit_button.click()

        # Fixed delay to wait for the complaint details page to load
        time.sleep(30)

        # Scrape the required details from the complaint details page
        # Example: Just printing the current URL as a placeholder
        # Replace the following line with your actual scraping logic
        print(driver.current_url)
        
    finally:
        # Close the browser session
        driver.quit()

# Streamlit UI
st.title("BBB Complaint Details Scraper")
complaint_code = st.text_input("Enter complaint code:")
if st.button("Scrape Details"):
    scrape_bbb_complaint_details(complaint_code)
