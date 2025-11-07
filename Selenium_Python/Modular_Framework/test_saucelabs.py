import pytest
from selenium import webdriver
from modules.login_module import LoginModule
from modules.inventory_module import InventoryModule


# ===== FIXTURES =====
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    return LoginModule(driver)


@pytest.fixture
def inventory(driver):
    return InventoryModule(driver)


# ===== TEST DATA =====
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
LOCKED_USERNAME = "locked_out_user"


# ===== LOGIN MODULE TESTS =====
class TestLoginModule:
    def test_successful_login(self, login, inventory):
        login.login(VALID_USERNAME, VALID_PASSWORD)
        assert login.is_login_successful() == True
        assert inventory.get_page_title() == "Products"

    def test_locked_user_login(self, login):
        login.login(LOCKED_USERNAME, VALID_PASSWORD)
        error_message = login.get_error_message()
        assert error_message is not None
        assert "locked out" in error_message

    def test_invalid_login(self, login):
        login.login("invalid_user", "wrong_password")
        error_message = login.get_error_message()
        assert error_message is not None
        assert "do not match" in error_message

    def test_empty_username(self, login):
        login.login("", VALID_PASSWORD)
        error_message = login.get_error_message()
        assert error_message is not None
        assert "Username is required" in error_message


# ===== INVENTORY MODULE TESTS =====
class TestInventoryModule:
    def test_inventory_page_loaded(self, login, inventory):
        login.login(VALID_USERNAME, VALID_PASSWORD)
        assert inventory.get_page_title() == "Products"
        assert inventory.get_product_count() == 6

    def test_product_list_displayed(self, login, inventory):
        login.login(VALID_USERNAME, VALID_PASSWORD)
        product_names = inventory.get_product_names()
        assert len(product_names) == 6
        assert "Sauce Labs Backpack" in product_names

    def test_add_product_to_cart(self, login, inventory):
        login.login(VALID_USERNAME, VALID_PASSWORD)
        assert inventory.add_product_to_cart("sauce-labs-backpack") == True
        assert inventory.get_cart_count() == 1

    def test_remove_product_from_cart(self, login, inventory):
        login.login(VALID_USERNAME, VALID_PASSWORD)
        inventory.add_product_to_cart("sauce-labs-backpack")
        assert inventory.get_cart_count() == 1
        assert inventory.remove_product_from_cart("sauce-labs-backpack") == True
        assert inventory.get_cart_count() == 0

    def test_logout_functionality(self, login, inventory, driver):
        login.login(VALID_USERNAME, VALID_PASSWORD)
        assert login.is_login_successful() == True
        assert inventory.logout() == True
        assert "saucedemo" in driver.current_url

