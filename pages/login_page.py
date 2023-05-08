import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN = (By.XPATH, "//a[@id='hrefUserIcon']")
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BTN = (By.XPATH, "//button[@type ='button']")
    ERROR_MESS = (By.XPATH, "//*[@id='signInResultMessage']")
    SEARCH = (By.XPATH, "//*[@id='menuSearch'][1]")
    VIEW = (By.XPATH, '//*[@id="output"]/div/div[2]/a[1]')
    SEARCH_BOX = (By.XPATH, "//*[@id='autoComplete']")
    ITEM_TABLETS = (By.XPATH,"//span[@id = 'tabletsTxt']")
    BUY_NOW = (By.XPATH, "//button[@name = 'buy_now']")
    ADD_TO_CART =(By.XPATH,"//button[@name = 'save_to_cart']")
    CART = (By.CSS_SELECTOR, "svg[id='menuCart']")
    PRODUCT_TEXT =(By.XPATH,"//label[@translate = 'PRODUCT_NAME']")
    REMOVE_ITEM = (By.XPATH, "//*[@id='product']/td[3]/div/div")
    EMPTY_CART_TEXT = (By.XPATH,"//*[@id='shoppingCart']/div/label")
    URL = "https://www.advantageonlineshopping.com/#/"

    def good_login(self, username, password):
        self.wait_and_click(*self.LOGIN)
        self.wait(*self.USERNAME_INPUT)
        self.fill_input(*self.USERNAME_INPUT, username)
        self.wait(*self.PASSWORD_INPUT)
        self.fill_input(*self.PASSWORD_INPUT, password)
        time.sleep(1)
        self.wait_and_click(*self.LOGIN_BTN)

    def bad_login(self, username, password):
        self.wait_and_click(*self.LOGIN)
        self.wait(*self.USERNAME_INPUT)
        self.fill_input(*self.USERNAME_INPUT, username)
        self.wait(*self.PASSWORD_INPUT)
        self.fill_input(*self.PASSWORD_INPUT, password)
        time.sleep(1)
        self.wait_and_click(*self.LOGIN_BTN)
        self.wait_error(*self.ERROR_MESS)

    def navigate_to_page(self):
        self.driver.get(self.URL)

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESS).text
