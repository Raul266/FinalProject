import time

from pages.login_page import LoginPage


class About(LoginPage):
    def about(self):
        self.wait_and_click(*self.SYMBOL)
        self.wait_and_click(*self.ABOUT)
        self.wait_site()