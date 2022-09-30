from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Cart is empty')
def verify_search_results (context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Your Amazon Cart is empty')]").text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got {actual_result}'
    print('test case passed')