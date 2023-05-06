from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    driver = webdriver.Chrome()
    driver.maximize_window()
    URL = ""

    def fill_input(self, by, selector, text):
        self.driver.find_element(by, selector).send_keys(text)

    def wait(self, by, selector):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by, selector)))

    def wait_and_click(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((by, selector)))
        self.driver.find_element(by, selector).click()

    def wait_error(self, by, selector):
        self.driver.implicitly_wait(5)
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((by, selector), "Incorrect user name or password."))

    def wait_site(self):
        WebDriverWait(self.driver,5).until(EC.url_changes('https://www.advantageonlineshopping.com/#/'))
        self.driver.implicitly_wait(5)

    def get_url(cls):
        return cls.URL
