import csv
import time
import random
from email import Email
from writeAndSend import writeAndSend

def listWriteAndSend(driver, csvFile, body, subject = ''):
    reader = csv.DictReader(csvFile)
    for row in reader:
        parsedBody = body.format(row['Name'])
        to = row['Email']
        email = Email(parsedBody, subject, to)
        writeAndSend(driver, email)
        #Sleep up to a minute
        time.sleep(random.choice([45,52,60]))