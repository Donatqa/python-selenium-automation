from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\\Users\\sirma\\OneDrive\\Desktop\\JobEasy\\python-selenium-automation\\chromedriver.exe')

#Open a page
driver.get('https://www.amazon.com/gp/help/customer/display.html')
driver.implicitly_wait(4)

driver.input_field = driver.find_element(By.ID, 'helpsearch')

driver.input_field.send_keys('Cancel order')
search_button = driver.find_element(By.XPATH, "//input[@class='a-button-input']")
search_button.click()

text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
assert text == 'Cancel Items or Orders'

driver.quit()