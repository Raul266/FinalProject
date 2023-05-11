Feature: Version

  Background:
    Given home: I am on the site

  @version
    Scenario: Test version
    When home: I click on the ? symbol at the top right of the site , after I click on AOS Versions
    Then version: I verify what version I have

     # Test 1: Test version