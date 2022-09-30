# Created by vyshnavisomisetty at 9/29/22
Feature: Test for amazon cart
  # Enter feature description here

  Scenario: User click amazon cart
    Given Open amazon page
    When Click on cart
    Then Cart is empty