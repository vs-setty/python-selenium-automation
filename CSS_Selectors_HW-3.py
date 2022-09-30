from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/vyshnavisomisetty/Automation/python-selenium-automation/chromedriver')
driver.get('https://www.amazon.com/ap/register?openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
#driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo").click()
#driver.find_element(By.CSS_SELECTOR, "h1[class='a-spacing-small']")
#driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
#driver.find_element(By.CSS_SELECTOR, "input[name='email']")
#driver.find_element(By.CSS_SELECTOR, "#ap_password")
#driver.find_element(By.CSS_SELECTOR, "#ap_password_check")
#driver.find_element(By.CSS_SELECTOR, "#continue")
#driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")
#driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")
#driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")
