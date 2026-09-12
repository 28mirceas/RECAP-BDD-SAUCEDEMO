from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


LOGIN_PAGE_URL = "https://www.saucedemo.com"

class LoginPage(BasePage):
    INPUT_USERNAME = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")
    ERROR_LOGIN_MESSAGE = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(LOGIN_PAGE_URL)

    def set_username(self, text):
        self.type(self.INPUT_USERNAME, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_button(self):
        self.click(self.BUTTON_LOGIN)

    def get_login_error_message_text(self):
        return self.get_text(self.ERROR_LOGIN_MESSAGE)

    #---------Verificari-------------------------


    def verify_login_error_message(self, expected_message):
        actual_message = self.get_login_error_message_text()

        assert actual_message == expected_message, (
            f"Expected error: {expected_message}, "
            f"but got: {actual_message}"
        )


    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_button()

        self.wait.until(EC.url_contains("inventory.html"))

        







