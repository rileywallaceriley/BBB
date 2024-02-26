from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scrape_bbb_complaint_details(complaint_code):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the BBB Response Portal login page
    login_page_url = "https://respond.bbb.org/respond/"
    print("Navigating to the login page:", login_page_url)
    driver.get(login_page_url)

    # Wait for the complaint code input field to be loaded
    print("Waiting for the complaint code input field to be loaded...")
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "cd"))
    )
    print("Complaint code input field is loaded.")

    # Enter the complaint code into the form
    print("Entering complaint code:", complaint_code)
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
    print("Complaint details page has loaded.")

    # Scrape the required details from the complaint details page
    # Add your scraping code here

    # Close the browser
    print("Closing the browser...")
    driver.quit()

# Example usage
complaint_code = "your_complaint_code_here"
scrape_bbb_complaint_details(complaint_code)
