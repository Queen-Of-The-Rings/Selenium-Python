from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import threading
import time


def simple_parallel_test():
    """Simple parallel execution without user input"""

    def run_chrome():
        print("🚀 Starting Chrome...")
        driver = webdriver.Remote(
            command_executor='http://localhost:4444',
            options=ChromeOptions()
        )
        run_test(driver, "Chrome")

    def run_edge():
        print("🚀 Starting Edge...")
        driver = webdriver.Remote(
            command_executor='http://localhost:4444',
            options=EdgeOptions()
        )
        run_test(driver, "Edge")

    def run_test(driver, browser_name):
        try:
            driver.get("https://www.saucedemo.com/")
            print(f"📄 {browser_name} - Page loaded: {driver.title}")

            # Login steps
            driver.find_element(By.ID, "user-name").send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")
            driver.find_element(By.ID, "login-button").click()

            time.sleep(2)

            # Verification
            if "inventory" in driver.current_url:
                print(f"✅ {browser_name} - Login SUCCESS")
            else:
                print(f"❌ {browser_name} - Login FAILED")

        except Exception as e:
            print(f"💥 {browser_name} - Error: {e}")
        finally:
            driver.quit()
            print(f"🔚 {browser_name} - Closed")

    # Start parallel execution
    chrome_thread = threading.Thread(target=run_chrome)
    edge_thread = threading.Thread(target=run_edge)

    chrome_thread.start()
    edge_thread.start()

    chrome_thread.join()
    edge_thread.join()

    print("🎉 Both browsers completed!")


if __name__ == "__main__":
    simple_parallel_test()