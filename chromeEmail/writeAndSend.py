from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random

def writeAndSend(driver, email):
    driver.find_element_by_xpath("//div[text()='COMPOSE']").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@role = 'dialog']")))
    driver.find_element_by_name("to").send_keys(email.to)
    driver.find_element_by_name("subjectbox").send_keys(email.subject)
    driver.find_element_by_xpath("//div[@role = 'textbox']").send_keys(email.body)
    #Stall some seconds
    time.sleep(random.choice([10,15,20]))
    #Send email
    driver.find_element_by_xpath("//div[text()='Send']").click()
    #Another stall
    time.sleep(random.choice([15,22,30]))