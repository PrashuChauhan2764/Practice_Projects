# import selenium
# print(selenium.__version__)
# exit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


#launch chrome
driver = webdriver.Chrome()

'''
#open google
driver.get("https://www.google.com")
time.sleep(3)
search = driver.find_element(By.NAME, "q")

#it search pyton for me on google
search.send_keys("Car")

#submit causes security error use keys.enter
#search.submit()
search.send_keys(Keys.ENTER)
#print(search)
print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(4)
driver.get("https://www.wikipedia.org")
time.sleep(3)
driver.back()
time.sleep(3)

#internship drr form it requires sign in google
#driver.get("https://forms.gle/RTAqZY5XYyF1p1LT6")

driver.forward()
time.sleep(3)
driver.refresh()

#to  find elements by name,id,class,css selector, xpath



#wait for 5 sec
time.sleep(4)

#to close the browser
driver.quit()
'''


'''
#now anti-robot website to check selenium features it enters username n paswd for me
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(3)
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
time.sleep(3)
login.click()
time.sleep(10)
driver.refresh()
driver.quit()
'''


#it waits until a condition is true
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Chrome() already declared
driver.get("https://the-internet.herokuapp.com/login")

heading = driver.find_element(By.TAG_NAME, "h2")
print(heading.text)

#PRINT THE LINK
link = driver.find_element(By.LINK_TEXT, "Form Authentication")
print(link.get_attribute("href"))

wait = WebDriverWait(driver, 10)
username = wait.until(
    EC.presence_of_element_located((By.ID, "username"))
)
password = wait.until(
    EC.presence_of_element_located((By.ID, "password"))

)
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
login = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)
login.click()
time.sleep(2)
driver.quit()

'''

# Handle special cases: alerts,pop-ups, frames,multiple tabs, dropdowns, checkboxes, radio button

'''
#for checkboxes
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(3)
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
checkboxes[0].click() #tick this one
time.sleep(3)
checkboxes[1].click() #untick this one
print(checkboxes[0].is_selected())
print(checkboxes[1].is_selected())
time.sleep(5)
driver.quit()
'''


'''
from selenium.webdriver.support.ui import Select

#for dropdowns
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(2)
dropdown = Select(driver.find_element(By.ID,"dropdown"))

#select option1
dropdown.select_by_visible_text("Option 1") #by visible text
dropdown.select_by_value("1") #by value
dropdown.select_by_index(1) #by index
time.sleep(2)

#select option 2
dropdown.select_by_visible_text("Option 2")
print(dropdown.first_selected_option.text)
time.sleep(5)
driver.quit()
'''


'''
#for alerts
#step1: simple alert [ok button] for alerts
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#click "Click for js alert"
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
time.sleep(2)

#switch to alert
alert = driver.switch_to.alert
#print alert text
print(alert.text)

#click ok
alert.accept()
time.sleep(3)


#step2: js confirm(ok/cancel button)
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
time.sleep(3)
alert = driver.switch_to.alert
alert.accept()
time.sleep(3)

#step3: Js prompt[type text]
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(3)

alert = driver.switch_to.alert

alert.send_keys("Prashu Chauhan")
time.sleep(3)

alert.accept()
#    OR
#alert.dismiss()
time.sleep(3)
result = driver.find_element(By.ID, "result")
print(result.text)
driver.quit()
'''

#for multiple windows
'''
driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(3)
#save the current parent tab
parent = driver.current_window_handle

#click click here
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(3)

#get all open tabs
all_tabs = driver.window_handles

#switch to the new tab
for tab in all_tabs:
    if tab != parent:
        driver.switch_to.window(tab)
        break

#print title of the new tab
print(driver.title)
time.sleep(3)

#close the new tab
driver.close()

#switch back to the parent tab
driver.switch_to_window(parent)

time.sleep(3)
print(driver.title)
driver.quit()
'''

#Frames
driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(3)
#switch into the iframe
driver.switch_to.frame("mce_0_ifr")

#fint the text area
#textbox = driver.find_element(By.ID, "tinymce")
textbox = driver.find_element(By.CSS_SELECTOR, "body")
print(textbox.tag_name)
print(textbox.get_attribute("contenteditable"))

#read the text
print(textbox.text)

#clear the textbox
textbox.send_keys(Keys.CONTROL, "a") #select all the text
time.sleep(3)
textbox.send_keys(Keys.BACKSPACE) #delete selected text
time.sleep(3)
#type new text
textbox.send_keys("Hello Prashu! This text was entered by Selenium.")

time.sleep(3)

#switch back to main page
driver.switch_to.default_content()
driver.quit()

