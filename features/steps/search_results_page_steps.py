from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Search results for coffee are shown')
def verify_search_results (context):
    expected_result = '"coffee"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Error! Expected {Expected_result} but got {actual_result}'