from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to simulate logging in and scraping complaint details
def scrape_bbb_complaint_details(complaint_code):
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Specify the path to chromedriver if not in PATH

    # Navigate to the BBB Response Portal login page
    login_page_url = "https://respond.bbb.org/respond/"
    driver.get(login_page_url)

    # Wait for the code input field to be loaded
    WebDriverWait(driver, 10).until(
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
    # This is an example, adjust the waiting condition based on your page's behavior
    WebDriverWait(driver, 10).until(
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

# Example usage
complaint_code = "your_complaint_code_here"  # Replace this with the actual code
scrape_bbb_complaint_details(complaint_code)
