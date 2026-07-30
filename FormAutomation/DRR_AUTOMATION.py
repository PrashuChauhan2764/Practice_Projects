#this pgm fill the sap id

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from datetime import date
import time
import os



script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "drr_data.json")


#load DRR data from the json file
with open(json_path, "r") as f:
    drr_data = json.load(f)


#INSTEAD OF TODAY I USSE SELECT DATE TO FILL DRR FOR
# today = date.today().strftime("%m/%d/%Y")
# if today not in drr_data:
#     raise ValueError(f"No DRR data found for {today}. Please add today's entry in drr_data.json")

# entry = drr_data[today]
# print(f"Loaded DRR data for {today}")


#SELECT DATE CHOICE
selected_date = input("Enter the DRR date to fill (MM/DD/YYYY): ").strip()
if selected_date not in drr_data:
    raise ValueError(f"No DRR data found for {selected_date}. Check drr_data.json entries.")

entry = drr_data[selected_date]
print(f"Loaded DRR data for {selected_date}")







   

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




#universal function version 1
# def fill_text(driver, label_text, value):

#     question = driver.find_element(
#         By.XPATH,
#         f"//span[contains(text(),'{label_text}')]/ancestor::div[contains(@class,'Qr7Oae')]"
#     )

#     try:
#         box = question.find_element(By.TAG_NAME, "textarea")
#     except NoSuchElementException:
#         box = question.find_element(By.TAG_NAME, "input")

#     box.clear()
#     box.send_keys(value)

#     print(f"{label_text} filled")



#version2 universal function
def fill_text(driver, label_text, value):

    question = driver.find_element(
        By.XPATH,
        f"//span[contains(text(),'{label_text}')]/ancestor::div[contains(@class,'Qr7Oae')]"
    )

    try:
        box = question.find_element(By.TAG_NAME, "textarea")
    except NoSuchElementException:
        box = question.find_element(By.TAG_NAME, "input")

    #scroll into view and wait until it's actually interactable
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", box)
    WebDriverWait(driver, 10).until(EC.visibility_of(box))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(box))

    box.clear()
    box.send_keys(value)

    print(f"{label_text} filled")





#radio button function
def select_radio(driver, question_text, option_text):

    question = driver.find_element(
        By.XPATH,
        f"//span[contains(text(),'{question_text}')]/ancestor::div[@jsname='WsjYwc']"
    )

    option = question.find_element(
        By.XPATH,
        f".//div[@role='radio' and @aria-label='{option_text}']"
    )

    driver.execute_script("arguments[0].click();", option)

    print(f"{option_text} selected")  


#function for file upload
def upload_file(driver, label_text, file_path):
    question = driver.find_element(
        By.XPATH,
        f"//span[contains(text(),'{label_text}')]/ancestor::div[@jsname='WsjYwc']"
    )

    #click the "Add file" button
    add_button = question.find_element(By.XPATH, ".//span[text()='Add file']")
    driver.execute_script("arguments[0].scrollIntoView(true);", add_button)
    driver.execute_script("arguments[0].click();", add_button)
    print("Add file button clicked")

    #wait for the upload iframe to appear
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src,'docs.google.com')]"))
    )
    driver.switch_to.frame(iframe)

    #find the file input inside the iframe and send the path
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    file_input.send_keys(file_path)
    print(f"{label_text} uploaded")

    time.sleep(3)
    driver.switch_to.default_content()


#function to toggle "Send me a copy of my responses"
def send_copy_checkbox(driver):
    checkbox = driver.find_element(
        By.XPATH,
        "//div[@role='checkbox' and @aria-label='Send me a copy of my responses.']"
    )
    if checkbox.get_attribute("aria-checked") == "false":
        driver.execute_script("arguments[0].click();", checkbox)
        print("Send me a copy - enabled")
    else:
        print("Send me a copy - already enabled")


#function to submit the form
def click_submit(driver):
    submit_button = driver.find_element(
        By.XPATH,
        "//div[@role='button' and @aria-label='Submit']"
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)
    print("Form submitted")

#function to sumbit another response
# def submit_another_response(driver):
#     link = driver.find_element(By.LINK_TEXT, "Submit another response")
#     driver.execute_script("arguments[0].click();", link)
#     print("Reloaded form for new response")




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


#FUNCTIONS CALL    
#page1------------------------------>
time.sleep(2)
fill_text(driver, "SAP Id", "590016978")
time.sleep(2)
fill_text(driver, "Name", "Prashu Chauhan")
time.sleep(2)
fill_text(driver, "College Mail Id", "Prashu.16978@stu.upes.ac.in")
time.sleep(4)
select_dropdown(driver,"School", "School of Computer Science")
time.sleep(2)
click_next(driver)


#page2------------------------------>
time.sleep(3)

#page 2
select_dropdown(driver, "Startup Name", "XO11 UAV SYSTEMS")
time.sleep(2)
#fill_date(driver, "Date", today)
fill_date(driver, "Date", selected_date)
time.sleep(2)
fill_text(driver, "Name of the Mentor", "krishna Pratap Singh")
time.sleep(2)
fill_text(driver,"Name of the Group Lead", "Kuber Jindal")
time.sleep(2)
click_next(driver)
time.sleep(3)



#new universal method for both input or textarea
fill_text(driver, "1. How did your day go?", entry["day"])
time.sleep(2)
fill_text(driver, "What task was assigned to you today?", entry["task"])
time.sleep(2)
# select_radio(
#     driver,
#     "Status of the task",
#     "In-progress"
# )


select_radio(driver,"Status of the task",entry["status"])


# select_radio(
#     driver,
#     "Status of the task",
#     "pending"
# )
time.sleep(2)
fill_text(driver,"What did you learn today? (Any new skill — technical, communication, teamwork, etc.)", entry["learning"])
time.sleep(2)
fill_text(driver,"Any challenge you faced? (What went wrong or felt difficult? How did you handle it?)", entry["challenge"])
time.sleep(2)
select_radio(driver,"On a scale of 1–10,",entry["rating"])
#select_radio(driver,"On a scale of 1–10","4")
# select_radio(driver,"On a scale of 1–10,","5")
# select_radio(driver,"On a scale of 1–10,","6")

#select_radio(driver,"Did you feel engaged and productive today?","Yes")
time.sleep(1)
select_radio(driver,"Did you feel engaged and productive today?",entry["engaged"])
time.sleep(2)
select_radio(driver,"SIO Name","Krishna Pratap Singh")
time.sleep(2)
upload_file(driver, "Geo Tag Photos", entry["photo"])
time.sleep(2)
send_copy_checkbox(driver)
time.sleep(2)

click_submit(driver)
time.sleep(2)

#call to another form response
#submit_another_response(driver)



#<------------end--------->
time.sleep(10)
driver.quit()