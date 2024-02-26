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
    driver.get(login_page_url)

    # Find and enter the complaint code into the form without waiting
    code_input = driver.find_element(By.ID, "cd")
    code_input.clear()
    code_input.send_keys(complaint_code)

    # Submit the form without waiting
    submit_button = driver.find_element(By.ID, "btn")
    submit_button.click()

    # Scrape the required details from the complaint details page without waiting
    # Replace these lines with code to scrape consumer information and complaint details

    # Close the browser
    driver.quit()

# Example usage
complaint_code = "632033975146E"
scrape_bbb_complaint_details(complaint_code)
