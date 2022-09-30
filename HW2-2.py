from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/vyshnavisomisetty/Automation/python-selenium-automation/chromedriver')
driver.get('https://www.amazon.com/')
driver.find_element(By .XPATH, "//span[text() = 'Returns']").click()
expected_result = 'Sign in'
actual_result = driver.find_element(By .XPATH, "//*[@class='a-spacing-small']").text
assert expected_result == actual_result, f'Error! Expected {Expected_result} but got {actual_result}'
print('test case passed')
driver.quit()