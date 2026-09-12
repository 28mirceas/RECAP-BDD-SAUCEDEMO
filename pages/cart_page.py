from pages.base_page import BasePage
from selenium.webdriver.common.by import By


CART_PAGE_URL = "https://www.saucedemo.com/cart.html"


class CartPage(BasePage):

    PRODUCT_ITEM = (By.CLASS_NAME, 'inventory_item')
    CART_LINK = (By.XPATH, '//a[@class="shopping_cart_link"]')
    CART_ITEM = (By.XPATH, '//div[@class="cart_item"]')
    BUTTON_CHECKOUT = (By.XPATH, '//button[@id="checkout"]')


    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart(self, product_name):
        product_items = self.find_multiple(self.PRODUCT_ITEM)

        for product_item in product_items:
            product_item_name = product_item.text.split('\n', 1)[:1][0]

            if product_item_name == product_name:

                product_name_button = (
                    By.XPATH,
                    f'//div[text()="{product_name}"]/parent::a/parent::div[@class="inventory_item_label"]/following-sibling::div[@class="pricebar"]//button'
                )

                self.click(product_name_button)



    def click_cart_link(self):
        print("========== CART DEBUG ==========")
        print("URL BEFORE:", self.driver.current_url)

        icon_link = self.driver.find_element(
            By.XPATH, '//a[@class="shopping_cart_link"]'
        )

        print("TAG:", icon_link.tag_name)
        print("TEXT:", repr(icon_link.text))
        print("CLASS:", icon_link.get_attribute("class"))

        icon_link.click()

        print("URL AFTER:", self.driver.current_url)



    def click_cart_checkout(self):
        print("========== CHECKOUT DEBUG ==========")
        print("URL BEFORE CHECKOUT:", self.driver.current_url)

        self.click(self.BUTTON_CHECKOUT)

        print("URL AFTER CHECKOUT:", self.driver.current_url)


    # ---------Verificari-------------------------

    def verify_cart_item_name(self, expected_cart_item_name):
        cart_items = self.find_multiple(self.CART_ITEM)

        for cart_item in cart_items:
            actual_cart_item_name = cart_item.text.split('\n', 2)[:2][1]

            assert actual_cart_item_name == expected_cart_item_name, (
                f"Expected error: {expected_cart_item_name}, "
                f"but got: {actual_cart_item_name}"
            )

