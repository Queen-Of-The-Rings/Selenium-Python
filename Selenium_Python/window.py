import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def simple_window_demo():
    driver = webdriver.Chrome()

    try:
        # Open parent window
        driver.get("https://demoqa.com/browser-windows")

        # Print parent details
        print("PARENT - Title:", driver.title)
        print("PARENT - Handle:", driver.current_window_handle)
        print("PARENT - URL:", driver.current_url)

        # Wait for page to load
        time.sleep(2)

        # Open child window using JavaScript click (bypasses the ad iframe)
        button = driver.find_element(By.ID, "windowButton")
        driver.execute_script("arguments[0].click();", button)
        print("Clicked button using JavaScript")
        time.sleep(2)

        # Get all windows and switch to child
        windows = driver.window_handles
        print(f"Total windows: {len(windows)}")

        # Switch to child window (the new window)
        driver.switch_to.window(windows[1])

        # Print child details
        print("CHILD - Title:", driver.title)
        print("CHILD - Handle:", driver.current_window_handle)
        print("CHILD - URL:", driver.current_url)

        # Close child and return to parent
        driver.close()
        print("Closed child window")

        # Switch back to parent
        driver.switch_to.window(windows[0])

        # Confirm return to parent
        print("BACK TO PARENT - Title:", driver.title)
        print("BACK TO PARENT - Handle:", driver.current_window_handle)
        print("Successfully completed!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()


simple_window_demo()