from selenium.webdriver.common.by import By
from selenium.webdriver.support.page_factory import FindBy


class LoginPage:
    # Locator variables using @FindBy annotation
    @FindBy(id="user-name")

    username_field = None

    @FindBy(id="password")

    password_field = None

    @FindBy(id="login-button")

    login_button = None

    @FindBy(className="error-message-container")

    error_message = None

    def __init__(self, driver):
        self.driver = driver
        from selenium.webdriver.support.page_factory import PageFactory
        PageFactory.init_elements(self.driver, self)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.username_field.clear()
        self.username_field.send_keys(username)

    def enter_password(self, password):
        self.password_field.clear()
        self.password_field.send_keys(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.error_message.text