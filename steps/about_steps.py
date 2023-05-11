from behave import *
from hamcrest import assert_that, equal_to

@given("home: I am on the main page")
def step_impl(context):
    context.version_page.navigate_to_page()
@when("home: I click on the ? symbol at the top right of the site , after I click on About")
def step_impl(context):
    context.about_page.about()
@then("about : I verify if I am on the correct URl")
def step_impl(context):
    assert_that(context.about_page.driver.current_url, equal_to("https://www.advantageonlineshopping.com/#/about"))