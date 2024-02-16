import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def run_selenium_script(customer_name):
    try:
        # Set up Chrome WebDriver with options
        options = Options()
        options.add_argument("--headless")  # For headless operation
        options.add_argument("--disable-gpu")  # Optional, for some headless environments
        options.add_argument("--no-sandbox")  # Bypass OS security model, required for Docker
        options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

        # Initialize Chrome WebDriver without using WebDriver Manager
        driver = webdriver.Chrome(options=options)

        # Retrieve username and password securely from environment variables
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')

        # Ensure credentials are not None
        if username is None or password is None:
            raise ValueError("Username or password environment variable is not set.")

        driver.get("https://www.bbb.org/kitchener/login")

        # Use explicit waits instead of fixed sleeps
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(username)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Log In')]"))).click()

        # Navigate and perform actions
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

        # Placeholder for further actions...

        return "Success - Actions completed"
    except NoSuchElementException as e:
        return f"Element not found error: {str(e)}"
    except TimeoutException as e:
        return f"Timeout error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    finally:
        # Quit the WebDriver session to release resources
        if 'driver' in locals():
            driver.quit()

# This section is optional for running as a standalone script
if __name__ == "__main__":
    # Example usage with a dummy customer name
    result = run_selenium_script("Example Customer")
    print(result)
