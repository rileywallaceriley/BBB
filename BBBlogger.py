import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def run_selenium_script(customer_name):
    # Retrieve username and password from Streamlit secrets
    username = st.secrets["bbb_credentials"]["username"]
    password = st.secrets["bbb_credentials"]["password"]
    
    # Path to chromedriver
    chromedriver_path = "./chromedriver"
    service = Service(executable_path=chromedriver_path)
    options = webdriver.ChromeOptions()
    # Configure Chrome options, including headless mode if necessary
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        # Log in and perform actions based on the customer name
        driver.get("https://www.bbb.org/kitchener/login")
        driver.find_element(By.NAME, "email").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        # Assuming there's a login button to click (adjust the selector as needed)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Your Selenium code to navigate and interact with the website goes here
        
        return "Success - Actions completed"
    except Exception as e:
        return f"An error occurred: {str(e)}"
    finally:
        driver.quit()

# Streamlit UI
st.title('Automated Web Interaction with Selenium')

# User provides only customer name
customer_name = st.text_input("Enter Customer Name", "")

if st.button("Run Automation"):
    if customer_name:
        result = run_selenium_script(customer_name)
        st.success(result)
    else:
        st.error("Please enter a customer name.")
