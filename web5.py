
from selenium import webdriver

driver = webdriver.Chrome('c:\\Work\\chromedriver')

driver.implicitly_wait(3)
driver.get('https://google.com')