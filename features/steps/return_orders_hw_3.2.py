from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click on orders and returns')
def click_orders_returns (context):
    context.driver.find_element(By.XPATH, "//span[text() = 'Returns']").click()