from behave import *
from hamcrest import assert_that, equal_to


@given('home: I am on page')
def step_impl(context):
    context.login_page.navigate_to_page()
@when('home: I click and I add an item to my cart')
def step_impl(context):
   context.cart_page.add_to_cart()
@then('products: I verify if I have an item in my cart')
def step_impl(context):
    assert_that(context.cart_page.product_text(),equal_to("PRODUCT NAME"))

@when('home: I click and I remove an item from my cart')
def step_impl(context):
    context.cart_page.remove_from_cart()
@then('products: I check if I have removed an item in my cart')
def step_impl(context):
    assert_that(context.cart_page.empty_cart_text(), equal_to('Your shopping cart is empty'))
