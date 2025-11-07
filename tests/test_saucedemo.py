import pytest
import sys
import os
from selenium import webdriver

# Add the project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Selenium_Python.pages.login_page import LoginPage
from Selenium_Python.pages.inventory_page import InventoryPage

class TestSauceDemo:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_successful_login(self, driver):
        login_page = LoginPage()
        login_page.open(driver)
        login_page.login(driver, "standard_user", "secret_sauce")

        inventory_page = InventoryPage()
        assert "inventory" in inventory_page.get_current_url(driver)
        assert inventory_page.get_page_title(driver) == "Products"
        assert inventory_page.get_inventory_count(driver) > 0
        print("test exeuted successfully")