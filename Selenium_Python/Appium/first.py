from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

print("🚀 Starting Simple Appium Test...")
print("Note: Make sure Appium server is running in another terminal!")

# Basic configuration
appium_server_url = 'http://localhost:4723'

try:
    print("1. Setting up capabilities...")

    # Create options - use EXACT automation name from installed drivers
    options = UiAutomator2Options()

    # Try different variations of automation_name
    options.platform_name = 'Android'
    options.automation_name = 'uiautomator2'  # lowercase
    options.device_name = 'emulator-5554'  # Use your actual device ID

    # For Android, we might not need app package/activity for basic connection
    # options.app_package = 'com.android.settings'
    # options.app_activity = '.Settings'

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

    # Print all capabilities to see what we're connected to
    print("📋 Connection Details:")
    for key, value in driver.capabilities.items():
        print(f"   {key}: {value}")

    # Simple test - get device time
    device_time = driver.device_time
    print(f"⏰ Device Time: {device_time}")

    # Take a screenshot
    driver.save_screenshot("connection_success.png")
    print("📸 Screenshot saved as 'connection_success.png'")

    print("🎉 Basic connection test PASSED!")
    time.sleep(2)

except Exception as e:
    print(f"❌ ERROR: {e}")
    print("\n🔧 Troubleshooting:")
    print("   1. Is Appium server running? Run 'appium' in another terminal")
    print("   2. Is emulator running? Check with 'adb devices'")
    print("   3. Check exact driver name with 'appium driver list --installed'")

finally:
    if 'driver' in locals():
        print("🛑 Closing driver...")
        driver.quit()
        print("✅ Driver closed")

print("🎯 Test completed!")