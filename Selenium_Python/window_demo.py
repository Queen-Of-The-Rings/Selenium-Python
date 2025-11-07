from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def simple_window_handling_demo():
    try:
        # Basic Chrome driver initialization
        driver = webdriver.Chrome()
        print("Chrome driver initialized successfully")

        # Navigate to the page
        driver.get("https://demoqa.com/browser-windows")
        print("Page title:", driver.title)

        # Get current window
        main_window = driver.current_window_handle
        print("Main window handle:", main_window)

        # Click to open new window
        driver.find_element(By.ID, "windowButton").click()
        time.sleep(3)  # Wait for new window

        # Get all windows
        all_windows = driver.window_handles
        print("All windows:", all_windows)

        # Switch to new window
        for window in all_windows:
            if window != main_window:
                driver.switch_to.window(window)
                print("New window title:", driver.title)
                print("New window URL:", driver.current_url)

                # Close new window and break
                driver.close()
                break

        # Switch back to main window
        driver.switch_to.window(main_window)
        print("Back to main window:", driver.title)

    except Exception as e:
        print("Error:", e)
        import traceback
        traceback.print_exc()
    finally:
        if 'driver' in locals():
            driver.quit()
            print("Done")


# Run the simple version
simple_window_handling_demo()