from selenium import webdriver

from selenium.webdriver.common.by import By

import time


def webdriver_methods_demo():
    driver = webdriver.Chrome()

    try:
        # Navigate to Google
        driver.get("https://www.google.com")
        # Get page title
        print(f"Title: {driver.title}")

        # Get current URL

        print(f"URL: {driver.current_url}")

        # Maximize window

        driver.maximize_window()

        time.sleep(2)

        # Set window size

        driver.set_window_size(800, 600)

        time.sleep(2)

        # Navigate to another site

        driver.get("https://www.python.org")

        time.sleep(2)

        # Go back to Google

        driver.back()

        time.sleep(2)

        # Go forward to Python

        driver.forward()

        time.sleep(2)

        # Refresh page

        driver.refresh()



    finally:

        driver.quit()


webdriver_methods_demo()