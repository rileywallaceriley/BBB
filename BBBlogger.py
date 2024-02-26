import streamlit as st
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scrape_bbb_complaint_details(complaint_code):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the BBB Response Portal login page
    login_page_url = "https://respond.bbb.org/respond/"
    driver.get(login_page_url)

    # Wait for the code input field to be loaded
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "cd"))
    )

    # Enter the complaint code into the form
    code_input = driver.find_element(By.ID, "cd")
    code_input.clear()
    code_input.send_keys(complaint_code)

    # Submit the form
    submit_button = driver.find_element(By.ID, "btn")
    submit_button.click()

    # Wait for the complaint details page to load
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.card-body"))
    )

    # Scrape the required details from the complaint details page
    # Adjust the selectors based on the actual content you need to scrape
    consumer_information = driver.find_element(By.CSS_SELECTOR, "div.consumer-information").text
    complaint_details = driver.find_element(By.CSS_SELECTOR, "div.complaint-details").text

    # Close the browser
    driver.quit()

    # Return scraped data
    return consumer_information, complaint_details

# Streamlit UI
st.title("BBB Complaint Details Scraper")
complaint_code = st.text_input("Enter complaint code:")
if st.button("Scrape"):
    consumer_information, complaint_details = scrape_bbb_complaint_details(complaint_code)
    st.write("Consumer Information:", consumer_information)
    st.write("Complaint Details:", complaint_details)
