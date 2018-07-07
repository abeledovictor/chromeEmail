import credentials
from settings import Settings
from email import Email
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

body = 'This is the body'
subject = 'This is the subject'
to = 'example@gmail.com'

email = Email(body, subject, to)


chromedriver_location = Settings.chromedriver_location

driver = webdriver.Chrome(chromedriver_location)

url = 'https://www.google.com/accounts/Login?hl=en&continue=http://www.google.com/'
driver.get(url)

#Login
driver.find_element_by_id("identifierId").send_keys(credentials.email)
driver.find_element_by_id("identifierNext").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
driver.find_element_by_name("password").send_keys(credentials.password)
driver.find_element_by_id("passwordNext").click()
#Go to Gmail
driver.get("https://www.gmail.com")

#Write email
driver.find_element_by_xpath("//div[text()='COMPOSE']").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@role = 'dialog']")))
driver.find_element_by_name("to").send_keys(email.to)
driver.find_element_by_name("subjectbox").send_keys(email.subject)
driver.find_element_by_xpath("//div[@role = 'textbox']").send_keys(email.body)
#Stall some seconds
time.sleep(10)
#Send email
driver.find_element_by_id(":8q").click()