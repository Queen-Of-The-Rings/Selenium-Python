from selenium import webdriver

from selenium.webdriver.common.by import By

import time


def javascript_executor_demo():
    driver = webdriver.Chrome()

    try:

        driver.get("https://www.saucedemo.com")

        # Login first

        driver.find_element(By.ID, "user-name").send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)

        # JavaScript Executor examples

        # 1. Scroll to bottom

        driver.execute_script("window.scrollTo(0, 700);")

        time.sleep(4)

        # 2. Scroll to top

        driver.execute_script("window.scrollTo(0, 0);")

        time.sleep(4)


    finally:

        driver.quit()


javascript_executor_demo()
