#this pgm fill the sap id

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


#function for text field
def fill_by_label(driver, label_text, value):
    question = driver.find_element(By.XPATH, f"//span[text()='{label_text}']/ancestor::div[@jsname='WsjYwc']"
    )
    textbox = question.find_element(By.TAG_NAME, "input") 
    textbox.clear()
    textbox.send_keys(value)   

#function for dropdown
def select_dropdown(driver, label_text, option_text):
    print("Finding question...")
    
    question = driver.find_element(By.XPATH, f"//span[contains(text(),'{label_text}')]/ancestor::div[@jsname='WsjYwc']" )
    print("Question found")
    dropdown = question.find_element(By.XPATH, ".//div[@role='listbox']")
    print("Clicking dropdown...")
    dropdown.click()

    time.sleep(3)
    print("Finding option...")

    #click the desired option
    option = driver.find_element(
    By.XPATH,
    f"//div[@role='option' and @data-value='{option_text}']")
    print("Option found")
    print(option.is_displayed())
    print(option.is_enabled())
    driver.execute_script("arguments[0].click();", option)
    print("Option clicked")

#function for next page
def click_next(driver):
    next_button = driver.find_element(By.XPATH, "//span[text()='Next']/ancestor::div[@role='button']")
    driver.execute_script("arguments[0].click();", next_button)
    print("Move to next page")

#function for date
def fill_date(driver, label_text, date_value):
    question = driver.find_element(By.XPATH, f"//span[contains(text(), '{label_text}')]/ancestor::div[@jsname='WsjYwc']")
    date_box = question.find_element(By.XPATH, ".//input[@type='date']")
    date_box.clear()
    date_box.send_keys(date_value)
    print(f"{label_text} filled")

#function for textarea
def fill_textarea(driver, label_text, value):
    question = driver.find_element(
        By.XPATH,
        f"//span[contains(text(),'{label_text}')]/ancestor::div[@jsname='WsjYwc']"
    )

    textarea = question.find_element(By.TAG_NAME, "textarea")

    textarea.clear()
    textarea.send_keys(value)

    print(f"{label_text} filled")

#universal function
def fill_text(driver, label_text, value):

    question = driver.find_element(
        By.XPATH,
        f"//span[contains(text(),'{label_text}')]/ancestor::div[contains(@class,'Qr7Oae')]"
    )

    try:
        box = question.find_element(By.TAG_NAME, "textarea")
    except:
        box = question.find_element(By.TAG_NAME, "input")

    box.clear()
    box.send_keys(value)

    print(f"{label_text} filled")

options = Options()
options.add_argument(r"--user-data-dir=C:\SeleniumProfile")

driver = webdriver.Chrome(options=options)
driver.maximize_window()
time.sleep(2)

driver.get("https://forms.gle/RTAqZY5XYyF1p1LT6")

time.sleep(2)

checkbox = driver.find_element(By.CSS_SELECTOR, 'div[role="checkbox"]')
print(checkbox.get_attribute("aria-checked"))
if checkbox.get_attribute("aria-checked") == "false":
    checkbox.click()

    
time.sleep(2)
fill_by_label(driver, "SAP Id", "590016978")
time.sleep(2)
fill_by_label(driver, "Name", "Prashu Chauhan")
time.sleep(2)
fill_by_label(driver, "College Mail Id", "Prashu.16978@stu.upes.ac.in")
time.sleep(4)
select_dropdown(driver,"School", "School of Computer Science")
time.sleep(2)
click_next(driver)
time.sleep(3)

#page 2
select_dropdown(driver, "Startup Name", "XO11 UAV SYSTEMS")
time.sleep(2)
fill_date(driver, "Date", "06-16-2026")
time.sleep(2)
fill_by_label(driver, "Name of the Mentor", "krishna Pratap Singh")
time.sleep(2)
fill_by_label(driver,"Name of the Group Lead", "Kuber Jindal")
time.sleep(2)
click_next(driver)
time.sleep(2)

# fill_textarea(
#     driver,
#     "1. How did your day go? (Briefly describe what you did today — meetings, tasks, field visits, research, etc.)",
#     "Met the client, discussed project requirements and completed documentation."
# )
# time.sleep(2)
# fill_by_label(driver,
#     "What task was assigned to you today?",
#     "Technical Research work."
# )

#new universal method for both input or textarea
fill_text(driver, "1. How did your day go?", "Met the client and completed documentation.")
time.sleep(2)
fill_text(driver, "What task was assigned to you today?", "Technical Research work.")







time.sleep(7)

driver.quit()