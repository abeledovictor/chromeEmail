import csv
import time
import random
from email import Email
from writeAndSend import writeAndSend

def listWriteAndSend(driver, csvFile, body, subject = ''):
    reader = csv.DictReader(csvFile)
    loopNumber = 1
    for row in reader:
        print('Sending E-mail number {}...'.format(loopNumber))
        parsedBody = body.format(row['Name'])
        to = row['Email']
        email = Email(parsedBody, subject, to)
        writeAndSend(driver, email)
        #Sleep up to 45 secs
        loopNumber+= 1
        time.sleep(random.choice([30,37,45]))