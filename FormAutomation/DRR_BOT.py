from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()

#Use my existing Chrome Profile
options.add_argument(r"--user-data-dir=C:\Users\Prashu Chauhan\AppData\Local\Google\Chrome\User Data")
options.add_argument("--profile-directory=Profile 1")


driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://forms.gle/RTAqZY5XYyF1p1LT6")
time.sleep(5)
driver.quit()