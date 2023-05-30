from behave import *
from hamcrest import assert_that, equal_to

@given('login: the user is on the login page')
def step_impl(context):
    context.login_page.navigate_to_page()

@when('login: user enters a valid {username} and {password} and presses login')
def step_impl(context,username,password):
    context.login_page.good_login(username,password)

@then('login: the user is on the home page')
def step_impl(context):
    assert_that(context.login_page.driver.current_url,
                equal_to("https://www.advantageonlineshopping.com/#/"))

@when('login: user  enters incorrect password  and clicks login')
def step_impl(context):
    context.login_page.bad_login("raul12345", "wrong")

@then('login: error message is displayed')
def step_impl(context):
    assert_that(context.login_page.get_error_message(),
                equal_to("Incorrect user name or password."))


@when('login: user enters incorrect {username} and correct {password} and clicks login')
def step_impl(context, username, password):
    context.login_page.bad_login(username, password)

@then('login: error message for incorrect username is displayed')
def step_impl(context):
    assert_that(context.login_page.get_error_message(),
    equal_to("Incorrect user name or password."))


@when('login: user enters incorrect {username} and {password} and clicks login')
def step_impl(context, username, password):
    context.login_page.bad_login(username, password)


@then('login: error message for incorrect credentials is displayed')
def step_impl(context):
    assert context.login_page.get_error_message() == "Incorrect user name or password."

