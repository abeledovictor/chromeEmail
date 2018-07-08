import credentials
from login import login
from endSession import endSession
from settings import Settings
from email import Email
from writeAndSend import writeAndSend
import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

body = 'This is the body'
subject = 'This is the subject'
to = 'example@gmail.com'
#Creates email to send
email = Email(body, subject, to)

#Creates a chromedriver session
chromedriver_location = Settings.chromedriver_location
driver = webdriver.Chrome(chromedriver_location)

#Login
login(driver,credentials.email,credentials.password)

#Write email
writeAndSend(driver, email)

#Logout
endSession(driver)
