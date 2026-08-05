'''from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

time.sleep(5)

driver.quit()'''


'''
to test with profile1
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()

options.add_argument(r"--user-data-dir=C:\Users\Prashu Chauhan\AppData\Local\Google\Chrome\User Data")
options.add_argument("--profile-directory=Profile 1")

# Prevent Chrome from trying to reuse an existing automation port
options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")

time.sleep(10)

driver.quit()

'''



