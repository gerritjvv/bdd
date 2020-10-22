Feature: Calculator Addition

  This simple feature is used to test Cucumber Studio integration

  Scenario: 1 + 1 is 3

    Given we have numbers
      | name | value |
      | a    | 1     |
      | b    | 2     |

    Then we expect addition results
      | name_1 | name_2 | equals |
      | a      | b      | 3      |
