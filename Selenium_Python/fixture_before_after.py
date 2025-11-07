# simplest_demo.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    print("👉 START Browser")
    driver = webdriver.Chrome()
    yield driver
    print("👋 CLOSE Browser")
    driver.close()


def test_sauce_demo_login(browser):
    """Test 1: Login to Sauce Demo practice website"""
    print("   Test 1: Testing Sauce Demo Login...")

    # Navigate to Sauce Demo practice website
    browser.get("https://www.saucedemo.com/")

    # Verify we're on login page
    assert "Swag Labs" in browser.title
    print("   ✓ Login page loaded")

    # Find login elements
    username_field = browser.find_element(By.ID, "user-name")
    password_field = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.ID, "login-button")

    # Enter credentials (standard test user)
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    # Verify login successful - should redirect to inventory page
    assert "inventory.html" in browser.current_url
    print("   ✓ Login successful - redirected to products page")

    # Verify products are displayed
    products = browser.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0
    print(f"   ✓ Found {len(products)} products")


def test_google_search(browser):
    """Test 2: Search on Google"""
    print("   Test 2: Testing Google Search...")

    # Navigate to Google
    browser.get("https://www.google.com")

    # Verify Google page title
    assert "Google" in browser.title
    print("   ✓ Google page loaded")

    # Find search box and verify it exists
    search_box = browser.find_element(By.NAME, "q")
    assert search_box.is_displayed()
    print("   ✓ Search box found")

    # Enter search term
    search_box.send_keys("Selenium WebDriver")
    print("   ✓ Entered search term")


def test_automation_practice_site(browser):
    """Test 3: Practice automation on demo site"""
    print("   Test 3: Testing Automation Practice Site...")

    # Navigate to practice automation website
    browser.get("https://the-internet.herokuapp.com/")

    # Verify page title
    assert "The Internet" in browser.title
    print("   ✓ Practice site loaded")

    # Find and click on "Form Authentication" link
    auth_link = browser.find_element(By.LINK_TEXT, "Form Authentication")
    auth_link.click()

    # Verify we're on login page
    assert "login" in browser.current_url
    print("   ✓ Navigated to login page")

    # Find login form elements
    username_field = browser.find_element(By.ID, "username")
    password_field = browser.find_element(By.ID, "password")

    assert username_field.is_displayed()
    assert password_field.is_displayed()
    print("   ✓ Login form elements found")