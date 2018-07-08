import credentials
from login import login
from settings import Settings
from email import Email
import time
import random
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

#Login
login(driver,credentials.email,credentials.password)

#Write email
driver.find_element_by_xpath("//div[text()='COMPOSE']").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@role = 'dialog']")))
driver.find_element_by_name("to").send_keys(email.to)
driver.find_element_by_name("subjectbox").send_keys(email.subject)
driver.find_element_by_xpath("//div[@role = 'textbox']").send_keys(email.body)
#Stall some seconds
time.sleep(random.choice([10,15,20]))
#Send email
driver.find_element_by_id(":8q").click()
#Another stall
time.sleep(random.choice([15,22,30]))