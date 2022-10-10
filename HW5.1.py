from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/vyshnavisomisetty/Automation/python-selenium-automation/chromedriver')
driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

expected_result = 5
actual_result = len(driver.find_elements(By .CSS_SELECTOR, "div[class*='nav-tab-all_styl'] a"))
print(actual_result)
assert expected_result == actual_result, f'Error! Expected {expected_result} but got {actual_result}'
print('test case passed')
driver.quit()