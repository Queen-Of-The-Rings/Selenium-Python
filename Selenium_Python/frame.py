from selenium import webdriver

from selenium.webdriver.common.by import By

import time


def frame_handling_demo():
    driver = webdriver.Chrome()

    try:

        driver.get("https://demoqa.com/frames")

        # Switch to frame by index

        driver.switch_to.frame("frame1")

        # Switch to frame by ID

        #driver.switch_to.frame("frame1")

        print("Switched to frame")

        # Get text from frame
        time.sleep(2)
        frame_locator = driver.find_element(By.XPATH, "//*[@id='sampleHeading']")
        frame_text=frame_locator.text
        print(f"Frame text: {frame_text}")

        # Switch back to main content

        driver.switch_to.default_content()

        print("Switched back to main content")

        # Switch to frame by ID/Name (if available)

        # driver.switch_to.frame("frame1")

        # Switch to frame by WebElement



    finally:

        driver.quit()


frame_handling_demo()