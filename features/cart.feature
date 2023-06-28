Feature: Cart

  Background:
    Given home: I am on page

  @add_to_cart
    Scenario: Test add to cart
    When home: I click and I add an item to my cart
    Then products: I verify if I have an item in my cart


  @remove_from_cart
    Scenario: Test remove form cart
    When home: I click and I remove an item from my cart
    Then products: I check if I removed an item from my cart

    # Test 1: Test add item to cart
    # Test 2: Test remove item from cart