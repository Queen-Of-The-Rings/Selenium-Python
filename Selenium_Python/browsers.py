from selenium import webdriver

import time

from selenium.webdriver.chrome.options import Options

# Chrome Browser
myoptions = Options()
myoptions.add_argument("--headless")

# Start browser with correct syntax
driver = webdriver.Chrome(options=myoptions)

driver.get("https://www.google.com")
expected_title = "Googles"
actual_title=driver.title
if expected_title == actual_title:
    print("Title is same. Title verification passed")
else:
    print("Title is not same. Title verification failed")

time.sleep(2)
driver.quit()

