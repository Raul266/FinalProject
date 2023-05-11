Feature: About

  Background:
    Given home: I am on the main page

    @about
    Scenario: Test click about
      When home: I click on the ? symbol at the top right of the site , after I click on About
      Then about : I verify if I am on the correct URl