import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_bbb_complaint_details(complaint_code):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://respond.bbb.org/respond/")
        print("Current URL:", driver.current_url)  # Debugging: Check you're on the correct page
        
        # Wait for the element to be present before proceeding
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "cd")))

        # If the element is inside an iframe, uncomment the next line and specify the correct iframe id or name
        # driver.switch_to.frame("iframe_id_or_name")
        
        code_input = driver.find_element(By.ID, "cd")
        code_input.clear()
        code_input.send_keys(complaint_code)
        
        submit_button = driver.find_element(By.ID, "btn")
        submit_button.click()
        
        # Wait for the next page to load or for a specific element on the next page to ensure it has loaded
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "someElementOnNextPage")))
        
        # Scrape the data you need here
        
    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()

# Replace 'your_complaint_code_here' with the actual complaint code
scrape_bbb_complaint_details('your_complaint_code_here')
