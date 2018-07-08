import credentials
from login import login
from endSession import endSession
from writeAndSend import writeAndSend
from settings import Settings
from email import Email
from selenium import webdriver
from listWriteAndSend import listWriteAndSend
#Opens csv file at assets/csvSource.csv (you can add a name and an email)
with open('../assets/csvSource.csv', 'r') as csvFile:

    #Creates a chromedriver session
    chromedriver_location = Settings.chromedriver_location
    driver = webdriver.Chrome(chromedriver_location)

    #Login
    login(driver,credentials.email,credentials.password)

    #Write email
    #if you add {0} in body, it will replace it with the name written at csv file
    listBody = "Hello {0} i'm a csv email"
    #you can omit the subject
    listSubject = "here at csv world"
    listWriteAndSend(driver, csvFile, listBody, listSubject)

    #Logout
    endSession(driver)

