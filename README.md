# chromeEmail
Chrome automatic gmail email sender with selenium

Personal project for educational use only

# Instructions
1. Download ```chromedriver``` for your system [from here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Extract the .*zip* file and put it in ```/assets``` folder.
2. You can see how to use the project API at ```exampleList.py``` and ```exampleSimple.py```

## Simple example
Create a ```credentials.py``` file inside ```chromeEmail``` folder with two variables: ```email``` and ```password```. They are used to log in to your gmail account.
```
email = 'put.your.email.here@gmail.com'

password = 'here.goes.your.password'
```
After that, open ```exampleSimple.py```. Replace ```body``` with the message you want to send by email. Then replace ```subject``` with the subject of your email. Replace ```to``` with the receiver.
```
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
```
Lastly, open terminal pointing to chromeEmail folder and run ```python exampleSimple.py```

## List of recipients example
Create a ```credentials.py``` file inside ```chromeEmail``` folder with two variables: ```email``` and ```password```. They are used to log in to your gmail account.
```
email = 'put.your.email.here@gmail.com'

password = 'here.goes.your.password'
```
After that, open ```assets/csvSource.csv```. Add the name and email of the people you want to reach with the program. **Do NOT** change the first row (The one with **Name** and **Email** written in it). Save your changes keeping *.csv* format.
Then open ```exampleList.py```, replace ```listBody``` with the text you want to send. You can use ```{0}``` notation to reference the **name** at the **.csv** associated to that specific recipient. Replace the subject at ```listSubject```.
```
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

```
Finally, open terminal pointing to chromeEmail folder and run ```python exampleList.py```
