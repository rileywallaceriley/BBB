import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def setup_driver():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()
    driver.get("https://respond.bbb.org/respond/")
    driver.set_window_size(1711, 850)  # Set the window size if necessary
    return driver

def submit_code(driver, code):
    # Locate the input field by its ID, click on it, and enter the code
    code_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cd")))
    code_input.click()
    code_input.send_keys(code)

    # Locate and click the submit button
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn")))
    submit_button.click()

    # Optional: Handling a modal dialog by closing it if it appears
    try:
        close_modal = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rwCloseButton")))
        close_modal.click()
    except:
        print("Modal dialog not present or could not be closed.")

def main():
    st.title('BBB Complaint Details Submission')
    
    # User input for the code
    code = st.text_input('Enter your complaint code:', '')
    submit = st.button('Submit')
    
    if submit and code:
        driver = setup_driver()
        submit_code(driver, code)
        st.success('Submitted successfully')
        # Optionally, close the driver after submission or retain it open for further operations
        # driver.quit()

if __name__ == "__main__":
    main()
