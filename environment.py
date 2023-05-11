from pages.about_page import About
from pages.cart_page import Cart
from pages.login_page import LoginPage
from pages.search_page import Search
from pages.version_page import Version


def before_all(context):
    context.login_page = LoginPage()
    context.search_page = Search()
    context.cart_page = Cart()
    context.version_page = Version()
    context.about_page = About()
