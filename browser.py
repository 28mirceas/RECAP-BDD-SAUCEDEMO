from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser:

    def __init__(self):

        chrome_options = Options()

        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def close(self):
        self.driver.quit()




