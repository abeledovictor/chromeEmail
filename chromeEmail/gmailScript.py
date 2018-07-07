
from settings import Settings
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

mail_address = ''
password = ''

chromedriver_location = Settings.chromedriver_location

driver = webdriver.Chrome(chromedriver_location)

url = 'https://www.google.com/accounts/Login?hl=ja&continue=http://www.google.co.jp/'
driver.get(url)

driver.find_element_by_id("identifierId").send_keys(mail_address)
driver.find_element_by_id("identifierNext").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
driver.find_element_by_name("password").send_keys(password)