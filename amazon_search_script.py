from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/vyshnavisomisetty/Automation/python-selenium-automation/chromedriver')
driver.get('https://www.amazon.com/')
#by ID
#driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')

#by XPATH
#driver.find_element(By .XPATH, "//a[@href='/ref=nav_logo']").click()
#driver.find_element(By .XPATH, "//a[@class='nav-logo-link nav-progressive-attribute']").click()

#by tag only
#driver.find_element(By .XPATH, "//input")

#by attribute only
#driver.find_element(By .XPATH, "//*[@href='/ref=nav_logo']").click()
#driver.find_element(By .XPATH, "//*[@class='nav-logo-link nav-progressive-attribute']").click()

#by text - didn't work
#driver.find_element(BY .XPATH, "//a[text()='Back to School']").click()

#by multiple attributes
#driver.find_element(By .XPATH, "//a[@class='nav-a  ' and @href='/backtoschool?ref_=nav_cs_bts']").click()

#contains
#driver.find_element(By .XPATH, "//a[contains(text(), 'Back to')]").click()
#driver.find_element(By .XPATH, "//a[contains(@href, 'backtoschool')]").click()

#by multiplte nodes
driver.find_element(By .XPATH, "//div[@id='nav-xshop-container']//a[contains(@href, 'new-releases')]").click()