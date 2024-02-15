import os
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def run_selenium_script(customer_name):
    # Temporarily hardcoded for testing purposes
    username = "rwallace@lendcare.ca"
    # Retrieve the password securely from Streamlit secrets
    password = "Fuckoffboo123@!@!"
    
    try:
        # Get the current directory path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Set the path to the ChromeDriver executable in the root folder
        chromedriver_path = os.path.join(current_dir, "chromedriver")
        
        # Check if the ChromeDriver executable exists at the specified path
        if os.path.exists(chromedriver_path):
            # Set up Chrome WebDriver with options
            options = Options()
            options.add_argument("--headless")  # Optional, for headless operation
            
            # Initialize Chrome WebDriver using the specified ChromeDriver executable path
            service = Service(chromedriver_path)
            driver = webdriver.Chrome(service=service, options=options)
        else:
            raise FileNotFoundError("ChromeDriver executable not found at the specified path.")
        
        driver.get("https://www.bbb.org/kitchener/login")
        
        # Use explicit waits instead of fixed sleeps
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(username)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Log In')]"))).click()

        # Navigate and perform actions
        # Example of navigating with explicit wait for URL change
        WebDriverWait(driver, 10).until(EC.
