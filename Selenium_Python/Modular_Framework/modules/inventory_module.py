from selenium.webdriver.common.by import By
import time


class InventoryModule:
    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "title").text
        except:
            return None

    def get_product_count(self):
        try:
            products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
            return len(products)
        except:
            return 0

    def get_product_names(self):
        try:
            products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
            return [product.text for product in products]
        except:
            return []

    def add_product_to_cart(self, product_name):
        try:
            add_button = self.driver.find_element(By.ID, f"add-to-cart-{product_name.lower().replace(' ', '-')}")
            add_button.click()
            return True
        except:
            return False

    def remove_product_from_cart(self, product_name):
        try:
            remove_button = self.driver.find_element(By.ID, f"remove-{product_name.lower().replace(' ', '-')}")
            remove_button.click()
            return True
        except:
            return False

    def get_cart_count(self):
        try:
            cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            return int(cart_badge.text)
        except:
            return 0

    def logout(self):
        try:
            self.driver.find_element(By.ID, "react-burger-menu-btn").click()
            time.sleep(1)
            self.driver.find_element(By.ID, "logout_sidebar_link").click()
            time.sleep(1)
            return True
        except:
            return False