from selenium.webdriver.common.by import By
import time


class LoginModule:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_saucedemo(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    def login(self, username, password):
        self.navigate_to_saucedemo()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        except:
            return None

    def is_login_successful(self):
        try:
            return "inventory" in self.driver.current_url
        except:
            return False