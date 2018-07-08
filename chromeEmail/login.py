from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def login(driver, email, password):
    try:
        url = 'https://www.google.com/accounts/Login?hl=en&continue=http://www.google.com/'
        driver.get(url)
        driver.find_element_by_id("identifierId").send_keys(email)
        driver.find_element_by_id("identifierNext").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_id("passwordNext").click()
        #Go to Gmail
        driver.get("https://www.gmail.com")
    except:
        print('Something went wrong, please check your credentials and/or chromeEmail/login.py file')
    finally:
        print('Login to {} successful'.format(email))