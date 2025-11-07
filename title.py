import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#from selenium.webdriver.chrome.options import Options

# Configure Chrome options for headless mode
myoptions = Options()
myoptions.add_argument("--headless")

# Start browser with correct syntax
driver = webdriver.Chrome(options=myoptions)

# Define website and expected title
website_url = "https://www.saucedemo.com"
expected_title = "Swag Labs"  # Fixed typo: "Swag Lab" → "Swag Labs"

print("🔍 VERIFYING WEBSITE TITLE")

# Navigate to the website
driver.get(website_url)
time.sleep(2)

# Get actual title
actual_title = driver.title

# Print results
print(f"\n🌐 Website: {website_url}")
print(f"📖 Expected Title: '{expected_title}'")
print(f"📖 Actual Title: '{actual_title}'")

# Verify title
if expected_title.lower() == actual_title.lower():
    print("✅ PASS : Title matches exactly!")
else:
    print("❌ FAIL : Title does not match")

# Close browser
driver.quit()