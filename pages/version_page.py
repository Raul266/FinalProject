from pages.login_page import LoginPage


class Version(LoginPage):
    def version(self):
        self.wait_and_click(*self.SYMBOL)
        self.wait_and_click(*self.VERSION)
        self.wait(*self.NR_VERSION)

    def get_version(self):
        return self.driver.find_element(*self.NR_VERSION).text