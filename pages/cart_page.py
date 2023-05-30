from pages.login_page import LoginPage


class Cart(LoginPage):
    def add_to_cart(self):
        self.wait_and_click(*self.ITEM_TABLETS)
        self.wait_and_click(*self.BUY_NOW)
        self.wait_and_click(*self.ADD_TO_CART)
        self.wait_and_click(*self.CART)
        self.wait(*self.PRODUCT_TEXT)

    def product_text(self):
        return self.driver.find_element(*self.PRODUCT_TEXT).text


    def remove_from_cart(self):
        self.wait_and_click(*self.ITEM_TABLETS)
        self.wait_and_click(*self.BUY_NOW)
        self.wait_and_click(*self.ADD_TO_CART)
        self.wait_and_click(*self.CART)
        self.wait_and_click(*self.REMOVE_ITEM)

    def empty_cart_text(self):
        return self.driver.find_element(*self.EMPTY_CART_TEXT).text

