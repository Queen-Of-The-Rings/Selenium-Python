from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def locators_demo():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com")

        home_text=driver.find_element(By.CSS_SELECTOR,"div.login_credentials[data-test='login-credentials']").text
        print(home_text)
        print(home_text)

        # 1. ID Locator
        #username = driver.find_element(By.ID, "user-name")
        username=driver.find_element(By.CSS_SELECTOR,"input[placeholder='Username']")
        username.send_keys("standard_user")

        # 2. NAME Locator
        password = driver.find_element(By.NAME, "password")
        password.send_keys("secret_sauce")

        # 3. CLASS_NAME Locator
        login_btn = driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        time.sleep(2)

        # 4. TAG_NAME Locator
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"Number of links: {len(links)}")

        # 5. LINK_TEXT Locator
        driver.get("https://the-internet.herokuapp.com")
        ab_testing_link = driver.find_element(By.LINK_TEXT, "A/B Testing")
        ab_testing_link.click()
        time.sleep(2)

        # 6. PARTIAL_LINK_TEXT Locator
        driver.back()
        test_link = driver.find_element(By.PARTIAL_LINK_TEXT, "A/B")
        test_link.click()
        time.sleep(2)
    finally:
        driver.quit()
locators_demo()