import streamlit as st
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scrape_bbb_complaint_details(complaint_code):
    print("Starting the scraping process...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the BBB Response Portal login page
    print("Navigating to the login page...")
    login_page_url = "https://respond.bbb.org/respond/"
    driver.get(login_page_url)

    # Wait for the code input field to be loaded
    print("Waiting for the code input field to be loaded...")
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "cd"))
    )
    print("Code input field is loaded.")

    # Enter the complaint code into the form
    print(f"Entering complaint code: {complaint_code}")
    code_input = driver.find_element(By.ID, "cd")
    code_input.clear()
    code_input.send_keys(complaint_code)

    # Submit the form
    print("Submitting the form...")
    submit_button = driver.find_element(By.ID, "btn")
    submit_button.click()

    # Wait for the complaint details page to load
    print("Waiting for the complaint details page to load...")
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.card-body"))
    )
    print("Complaint details page is loaded.")

    # Scrape the required details from the complaint details page
    print("Scraping consumer information and complaint details...")
    consumer_information = driver.find_element(By.CSS_SELECTOR, "div.consumer-information").text
    complaint_details = driver.find_element(By.CSS_SELECTOR, "div.complaint-details").text

    print("Consumer Information:", consumer_information)
    print("Complaint Details:", complaint_details)

    # Close the browser
    print("Closing the browser...")
    driver.quit()

    print("Scraping process completed.")

# Streamlit UI
st.title("BBB Complaint Details Scraper")
complaint_code = st.text_input("Enter complaint code:")
if st.button("Scrape"):
    scrape_bbb_complaint_details(complaint_code)
