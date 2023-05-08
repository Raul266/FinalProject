import time

from pages.login_page import LoginPage


class Search(LoginPage):

    def search(self, query):
        self.wait_and_click(*self.SEARCH)
        self.wait(*self.SEARCH)
        self.fill_input(*self.SEARCH_BOX, query)
        self.wait(*self.VIEW)
        self.wait_and_click(*self.VIEW)
        self.wait_site()
