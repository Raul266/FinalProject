from pages.login_page import LoginPage
from pages.search_page import Search


def before_all(context):
    context.login_page = LoginPage()
    context.search_page = Search()

