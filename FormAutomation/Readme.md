### About Selenium
# More features to add:
1. make find_question function






Step 1 (Done) ✅

Open and close a browser.

You learned:

webdriver.Chrome()
driver.get()
driver.quit()

-------

Step 2: Control the browser

Learn how to:

Open different websites.
Go back.
Go forward.
Refresh the page.
Maximize the browser.
Change the window size.
Read the page title.
Read the current URL.
------------

Step 3: Find elements ⭐ (Most Important)

Everything in Selenium comes down to this.

A webpage contains elements like:

buttons
text boxes
links
images
checkboxes
dropdowns
eg: driver.find_element(...)
Different ways to find elements:

ID
Name
Class Name
CSS Selector
XPath

For example:search = driver.find_element(By.NAME, "q")

-------------
Step 4: Interact with elements

Once you find an element, you can:

.send_keys()
.click()
.clear()
.submit()

Example:

search.send_keys("Python")
search.submit()
--------------

Step 5: Waits

One of the biggest beginner mistakes is using only:

time.sleep(5)

Instead, you'll learn:

WebDriverWait
ExpectedConditions

These wait until something actually appears, making your automation faster and more reliable.

-------------
Step 6: Read information

Extract data from a webpage.

Example:

print(driver.title)

print(element.text)

print(element.get_attribute("href"))

What each one is for
driver.title → Reads information about the entire page (the browser tab title).
element.text → Reads the visible text inside an element.
element.get_attribute("href") → Reads the value of a specific HTML attribute (like href, id, class, type, value, etc.).

-------------------
Step 7: Handle special cases

Later you'll learn:

Alerts
Pop-ups
Frames
Multiple tabs
Dropdowns
Checkboxes
Radio buttons

-------------
Step 8: Real automation

Only after the basics should you automate tasks like:

Login forms
Google searches
Filling Google Forms
GitHub login
LinkedIn automation
Daily attendance forms


Quick rule:

Read text or inspect element → presence_of_element_located()
Type into an input → visibility_of_element_located() (commonly used)
Click a button → element_to_be_clickable()