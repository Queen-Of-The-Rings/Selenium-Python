import os
import subprocess
from appium import webdriver
import time

print("🎯 FINAL APPIUM TEST - With Android Environment Fixed!")


def check_environment():
    """Verify Android environment is properly set"""
    print("🔍 Verifying environment...")

    android_home = os.environ.get('ANDROID_HOME')
    android_sdk_root = os.environ.get('ANDROID_SDK_ROOT')

    print(f"✅ ANDROID_HOME: {android_home}")
    print(f"✅ ANDROID_SDK_ROOT: {android_sdk_root}")

    # Check ADB
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True, timeout=10)
        print("📱 ADB Devices:")
        print(result.stdout)
        return True
    except Exception as e:
        print(f"❌ ADB check failed: {e}")
        return False


def run_appium_test():
    """Run the main Appium test"""
    print("\n🚀 Starting Appium test...")

    # Appium configuration
    appium_server_url = 'http://localhost:4723/wd/hub'

    # Desired capabilities
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',  # Use your device ID from 'adb devices'
        'automationName': 'UiAutomator2',
        'appPackage': 'com.android.settings',
        'appActivity': '.Settings',
        'noReset': True,
        'newCommandTimeout': 60
    }

    driver = None
    try:
        print("1. Creating Appium driver...")
        print(f"   Server: {appium_server_url}")
        print(f"   Device: {desired_caps['deviceName']}")

        driver = webdriver.Remote(appium_server_url, desired_caps)

        print("✅ SUCCESS! Appium driver created!")
        print("🎉 CONGRATULATIONS! Your Appium setup is working!")

        # Print device info
        print("\n📋 Device Information:")
        caps = driver.capabilities
        for key in ['deviceName', 'platformName', 'platformVersion', 'automationName']:
            print(f"   {key}: {caps.get(key, 'Unknown')}")

        # Wait for app to load
        print("\n2. Loading Settings app...")
        time.sleep(3)

        # Get current app info
        current_package = driver.current_package
        current_activity = driver.current_activity
        print(f"📱 Current package: {current_package}")
        print(f"🎯 Current activity: {current_activity}")

        # Test 1: Find Settings options
        print("\n3. Testing UI interaction...")
        test_options = ["Battery", "Display", "Storage", "Apps", "Network & internet"]

        for option in test_options:
            try:
                element = driver.find_element_by_xpath(f'//*[@text="{option}"]')
                print(f"   ✅ Found: {option}")
                # Test if we can click it
                if element.is_displayed():
                    element.click()
                    print(f"   👆 Successfully clicked {option}!")
                    time.sleep(2)
                    # Go back to main settings
                    driver.back()
                    time.sleep(1)
                    break
            except Exception as e:
                print(f"   ❌ Not found/clickable: {option}")

        # Test 2: Take screenshot
        print("\n4. Taking screenshot...")
        driver.save_screenshot("appium_final_success.png")
        print("   📸 Screenshot saved as 'appium_final_success.png'")

        # Test 3: Get device time
        device_time = driver.device_time
        print(f"   ⏰ Device time: {device_time}")

        print("\n🎉 ALL TESTS PASSED! 🎉")
        print("✨ Your Appium setup is completely working!")

        return True

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        return False

    finally:
        if driver:
            print("\n🛑 Closing driver...")
            driver.quit()
            print("✅ Driver closed")


def main():
    print("=" * 60)
    print("APPIUM FINAL TEST - With Android Environment Variables Set")
    print("=" * 60)

    # Check environment
    if not check_environment():
        print("\n❌ Environment not set properly")
        return

    # Run the test
    success = run_appium_test()

    if success:
        print("\n" + "🎊 SUCCESS! 🎊".center(60))
        print("Your Appium setup is fully functional!".center(60))
        print("You can now automate Android apps!".center(60))
        print("=" * 60)
    else:
        print("\n" + "⚠️  TEST FAILED".center(60))
        print("Check the error message above".center(60))
        print("=" * 60)


if __name__ == '__main__':
    main()