from selenium import webdriver

from selenium.webdriver.common.by import By

import time


def alerts_demo():
    driver = webdriver.Chrome()

    try:

        driver.get("https://demoqa.com/alerts")

        # 1. Simple Alert

        button1 = driver.find_element(By.ID, "alertButton")

        #simple_alert_btn.click()
        driver.execute_script("arguments[0].click();", button1)
        time.sleep(1)

        # Switch to alert and accept
        a1 = driver.switch_to.alert
        print(f"Alert text: {a1.text}")
        a1.accept()

        print("Simple alert accepted")

        time.sleep(1)


        # 2. Confirmation Alert

        confirm_alert_btn = driver.find_element(By.ID, "confirmButton")

        #confirm_alert_btn.click()
        driver.execute_script("arguments[0].click();", confirm_alert_btn)

        time.sleep(1)

        a2 = driver.switch_to.alert

        print(f"Confirm alert text: {a2.text}")

        a2.dismiss()  # Try accept() for OK

        print("Confirmation alert dismissed")

        time.sleep(1)

        # 3. Prompt Alert

        prompt_alert_btn = driver.find_element(By.ID, "promtButton")

        #prompt_alert_btn.click()
        driver.execute_script("arguments[0].click();", prompt_alert_btn)

        time.sleep(2)

        a3 = driver.switch_to.alert
        time.sleep(2)
      #  alert.send_keys("christy")
        a3.send_keys("Selenium Python")
        time.sleep(2)

        print("Text entered in prompt")

        a3.accept()

        print("Prompt alert accepted")




    finally:

        driver.quit()


alerts_demo()