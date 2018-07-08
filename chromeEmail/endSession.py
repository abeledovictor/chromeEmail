
def endSession(driver):
    driver.delete_all_cookies()
    driver.quit()
    print("Session ended :D")