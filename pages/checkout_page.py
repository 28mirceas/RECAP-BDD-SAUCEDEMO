from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    CART_ITEM_PRICE = (By.XPATH, '//div[@class="inventory_item_price"]')
    INPUT_FIRST_NAME = (By.ID, "first-name")
    INPUT_LAST_NAME = (By.ID, "last-name")
    INPUT_POSTAL_CODE = (By.ID, "postal-code")
    BUTTON_CONTINUE = (By.XPATH, '//button[@id="continue"]')
    TOTAL_ITEMS_PRICE = (By.XPATH, '//div[@class="summary_subtotal_label"]')


    def __init__(self, driver):
        super().__init__(driver)
        

    def calculate_total_price(self):
        total_cart_items_price = 0
        cart_items_price = self.find_multiple(self.CART_ITEM_PRICE)
        for cart_item_price in cart_items_price:
            item_price = float(cart_item_price.text.replace("$", ""))
            total_cart_items_price += item_price
        return total_cart_items_price


    def set_checkout_first_name(self, text):
        self.type(self.INPUT_FIRST_NAME, text)


    def set_checkout_last_name(self, text):
        self.type(self.INPUT_LAST_NAME, text)


    def set_checkout_postal_code(self, text):
        self.type(self.INPUT_POSTAL_CODE, text)


    def click_checkout_continue(self):
        button = self.driver.find_element(By.ID, "continue")
        button.click()


    def get_checkout_items_price(self):
        text = self.get_text(self.TOTAL_ITEMS_PRICE)
        price = text.split("$")[1]
        return float(price)

    # ---------Verificari-------------------------

    def verify_total_checkout_items_price(self):
        expected_total_items_price = self.calculate_total_price()
        actual_total_items_price = self.get_checkout_items_price()

        assert actual_total_items_price == expected_total_items_price, (
            f"Expected error: {expected_total_items_price}, "
            f"but got: {actual_total_items_price}"
        )
