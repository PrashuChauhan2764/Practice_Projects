#chrome new selenium profile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()

# Use the dedicated Selenium profile
options.add_argument(r"--user-data-dir=C:\SeleniumProfile")

driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("https://forms.gle/RTAqZY5XYyF1p1LT6")

time.sleep(20)

driver.quit()