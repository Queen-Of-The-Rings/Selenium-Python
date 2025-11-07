from selenium import webdriver

from selenium.webdriver.common.by import By

import time


def webelement_methods():
    driver = webdriver.Chrome()

    try:

        driver.get("https://www.saucedemo.com")

        # Find element

        username = driver.find_element(By.ID, "user-name")

        # 1. send_keys() - Enter text

        username.send_keys("standard_user")

        # 2. clear() - Clear text

        username.clear()

        username.send_keys("problem_user")

        # 3. click() - Click element

        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        time.sleep(2)
        error_locator=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        error_text=error_locator.text
        print(f"error message: {error_text}")



    finally:

#        driver.quit()
         print("execution completed")

webelement_methods()