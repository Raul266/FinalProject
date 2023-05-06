Feature: Login feature
#user story

  #acceptance criteria
  Background:
    Given login: the user is on the login page

  @validcreds
  Scenario Outline: Login with valid credentials
    When login: user enters a valid <username> and <password> and presses login
    Then login: the user is on the home page

    Examples:
      | username  | password  |
      | raul12345 | Test12345 |

  @invalidpass
  Scenario: Login with invalid password
    When login: user  enters incorrect password  and clicks login
    Then login: error message is displayed

  @invalidusername
  Scenario Outline: Login with invalid username
    When login: user enters incorrect <username> and correct <password> and clicks login
    Then login: error message for incorrect username is displayed

    Examples:
      | username | password |
      | alabala  | alabala  |
      | raul     | raul     |

  @invalidcreds
  Scenario Outline: Login with invalid credentials
    When login: user enters incorrect <username> and <password> and clicks login
    Then login: error message for incorrect credentials is displayed

    Examples:
      | username | password |
      | alabala  | alabala  |
      | raul     | raul     |


      # test 1: login with invalid username
      # test 2: login with invalid credentials (parametrizat, mai multe valori)
      # test 3: login without empty username/password (parametrizat, mai multe valori)