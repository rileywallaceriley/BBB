from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scrape_bbb_complaint_details():
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

    # Get complaint code from the user
    complaint_code = input("Enter complaint code: ")

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

    print("Consumer Information:", consumer_information)
    print("Complaint Details:", complaint_details)

    # Close the browser
    driver.quit()

# Call the function to start the scraping process
scrape_bbb_complaint_details()
