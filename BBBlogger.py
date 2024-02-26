import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def scrape_details(code):
    # Initialize the Chrome driver with webdriver-manager
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    
    try:
        # Navigate to the page and interact with it
        driver.get("https://respond.bbb.org/respond/")
        
        # Wait for the input field and enter the code, adjust selector as needed
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "input_code_name"))  # Adjust the selector
        ).send_keys(code)
        
        # Submit the form, adjust the selector as needed
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        # Wait for the navigation to complete, adjust the condition as needed
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='customer_details']"))  # Adjust the selector
        )
        
        # Scrape required details
        customer_details = driver.find_element(By.ID, "customer_details").text  # Adjust the selector
        complaint = driver.find_element(By.ID, "complaint_text").text  # Adjust the selector
        
        return {"customer_details": customer_details, "complaint": complaint}
    except Exception as e:
        return {"error": str(e)}
    finally:
        driver.quit()

# Streamlit UI
st.title('BBB Complaint Details Scraper')

code = st.text_input("Enter Code", "")

if st.button("Scrape Details"):
    if code:
        result = scrape_details(code)
        
        if "error" in result:
            st.error("Failed to scrape details: " + result["error"])
        else:
            st.success("Scraping successful!")
            st.subheader("Customer Details:")
            st.write(result["customer_details"])
            st.subheader("Complaint:")
            st.write(result["complaint"])
    else:
        st.error("Please enter a code.")
