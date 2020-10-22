Feature: Calculator Subtract

  This simple feature is used to test Cucumber Studio integration

  Scenario: 1 - 1 is 0

    Given we have numbers
      | name | value |
      | a    | 1     |
      | b    | 1     |

    Then we expect subtraction results
      | name_1 | name_2 | equals |
      | a      | b      | 0      |
