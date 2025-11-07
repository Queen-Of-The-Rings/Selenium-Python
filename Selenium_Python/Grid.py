from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def basic_grid_test():
    print("🚀 Starting Basic Grid Test...")

    try:
        # Most basic remote driver - let Grid handle everything
        driver = webdriver.Remote(
            command_executor='http://localhost:4444',
            options=webdriver.ChromeOptions()  # Let Grid use default Chrome
        )

        print("✅ Connected to Grid successfully")

        # Test steps
        driver.get("https://www.saucedemo.com/")
        print(f"📄 Page title: {driver.title}")

        # Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)

        # Check if login worked
        if "inventory" in driver.current_url:
            print("✅ TEST PASSED - Login successful!")
        else:
            error_text = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
            print(f"❌ TEST FAILED - {error_text}")

    except Exception as e:
        print(f"💥 ERROR: {e}")

    finally:
        if 'driver' in locals():
            driver.quit()
            print("🔚 Browser closed")


if __name__ == "__main__":
    basic_grid_test()