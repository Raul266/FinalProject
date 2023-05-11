from behave import *
from hamcrest import assert_that, equal_to

@given("home: I am on the site")
def step_impl(context):
    context.version_page.navigate_to_page()
@when("home: I click on the ? symbol at the top right of the site , after I click on AOS Versions")
def step_impl(context):
    context.version_page.version()
@then("version: I verify what version I have")
def step_impl(context):
    assert_that(context.version_page.get_version(),equal_to("VERSION 3.2"))