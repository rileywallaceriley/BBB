import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Function to setup the Chrome WebDriver
def setup_driver():
    # Add the path to the ChromeDriver if it's not in the default PATH
    # Example: driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver = webdriver.Chrome()
    return driver

# Function to navigate and scrape data
def scrape_bbb_complaint_details(complaint_id):
    driver = setup_driver()
    try:
        # Navigating to the page
        driver.get("https://respond.bbb.org/respond/")
        driver.set_window_size(1024, 768) # Adjust size as needed

        # Interacting with the page
        time.sleep(2)  # Adjust based on page load time
        code_input = driver.find_element(By.ID, "cd")
        code_input.click()
        code_input.send_keys(complaint_id)
        
        submit_btn = driver.find_element(By.ID, "btn")
        submit_btn.click()

        # Add any additional interactions here

        # Example: Copy content
        # content = driver.find_element(By.YOUR_SELECTOR).text
        # print(content)  # or return it

    finally:
        driver.quit()

# Streamlit UI
def main():
    st.title('BBB Complaint Details Scraper')
    complaint_id = st.text_input('Enter the Complaint ID:', '')
    
    if st.button('Scrape Details'):
        if complaint_id:
            scrape_bbb_complaint_details(complaint_id)
            # Display the scraped data
            # st.write(content)
        else:
            st.error('Please enter a valid Complaint ID.')

if __name__ == '__main__':
    main()
