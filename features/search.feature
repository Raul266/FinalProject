Feature:  search feature

  Background:
    Given home: I am a user on page

  @search_tablets
  Scenario Outline: Test search functionality
    When home: I search after <query>
    Then products: I verify if I found what I wanted

    Examples:
      | query   |
      | tablets |

  @search_laptop
  Scenario: Test search functionality
    When home: I search laptop
    Then products: I verify if I found laptop on the site

    # test 1: test search tablets
    # test 2: test search laptop
