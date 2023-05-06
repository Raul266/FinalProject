from behave import *
from hamcrest import assert_that, equal_to


@given("home: I am a user on page")
def step_impl(context):
    context.search_page.navigate_to_page()


@when('home: I search after {query}')
def step_impl(context, query):
    context.search_page.search(query)


@then('products: I verify if I found what I wanted')
def step_impl(context):
    assert_that(context.search_page.driver.current_url,
                equal_to("https://www.advantageonlineshopping.com/#/search/?viewAll=tablets"))


@when('home: I search laptop')
def step_impl(context):
    context.search_page.search("laptop")


@then('products: I verify if I found laptop on the site')
def step_impl(context):
    assert_that(context.search_page.driver.current_url,
                equal_to("https://www.advantageonlineshopping.com/#/search/?viewAll=laptop"))
