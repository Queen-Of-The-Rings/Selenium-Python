from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

print("🚀 Starting Appium Test with Correct Driver Configuration...")

appium_server_url = 'http://localhost:4723'

try:
    print("1. Setting up capabilities...")

    # Create options
    options = UiAutomator2Options()

    # Use the exact automation name that matches the installed driver
    options.platform_name = 'Android'
    options.automation_name = 'UIAutomator2'  # Capital U, capital A
    options.device_name = 'emulator-5554'

    # Add app capabilities
    options.app_package = 'com.android.settings'
    options.app_activity = '.Settings'

    print("2. Connecting to Appium server...")
    print(f"   Server: {appium_server_url}")
    print(f"   Platform: {options.platform_name}")
    print(f"   Automation: {options.automation_name}")
    print(f"   Device: {options.device_name}")

    driver = webdriver.Remote(
        command_executor=appium_server_url,
        options=options
    )

    print("✅ SUCCESS: Appium driver created!")

    # Print capabilities
    print("📋 Connection Details:")
    for key, value in driver.capabilities.items():
        print(f"   {key}: {value}")

    # Simple test
    device_time = driver.device_time
    print(f"⏰ Device Time: {device_time}")

    driver.save_screenshot("success.png")
    print("📸 Screenshot saved!")

    print("🎉 Test PASSED!")
    time.sleep(3)

except Exception as e:
    print(f"❌ ERROR: {e}")

finally:
    if 'driver' in locals():
        driver.quit()
        print("✅ Driver closed")