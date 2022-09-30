# Created by vyshnavisomisetty at 9/26/22
Feature: Tests for amazon search
  # Enter feature description here

  Scenario: User can search for a product
    Given Open amazon page
    When Search for coffee
    Then Search results for coffee are shown
