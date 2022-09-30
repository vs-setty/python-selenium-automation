from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click on cart')
def click_cart (context):
    context.driver.find_element(By.CSS_SELECTOR, ".nav-cart-icon.nav-sprite").click()