# 1. How to handle Dropdowns in selenium? Explain different types in dropdown value selection.
import time

# Answer :
# There are various types of dropdowns available these days, majorly of which are categorized as a single-select (which allows selecting only one value) or multi-select (which allows selecting multiple values).
# Selenium WebDriver provides a class named "Select", which provides various methods to handle the dropdowns, be it single-select or multi-select dropdowns.


# In HTML, the static dropdowns are generally implemented either using the <select> tag
#
# We should use [Select] class provided by the "org.openqa.selenium.support.ui " package of Selenium WebDriver to handle the elements of the dropdown
#
# We should create an object to the select class , so that we can access the methods of select class

# "Select " class is provided by the "org.openqa.selenium.support.ui " package of Selenium WebDriver.

# Example :  #
# dropdown = Select(driver.find_element(By.XPATH,"//*[@data-style='btn-info']"))#
# There are different methods in the Select class to help in element access
#
# Example :
#
# dropdown.select_by_value()  - This is select the dropdown by its value
# dropdown.select_by_index() - This is select the dropdown by its index ( Say first index as 0)
# dropdown.select_by_visible_text() - This is select the dropdown by its visible Text (Say, India)
# dropdown.all_selected_options - This is to get the list of all selected option
# dropdown.first_selected_option - This is to get first selected option only
# dropdown.deselect_all() - This is to deselect all the option
# dropdown.deselect_by_index() -  This is de-select the dropdown by its index
# dropdown.deselect_by_value() - This is de-select the dropdown by its value
# dropdown.deselect_by_visible_text() - This is de-select the dropdown by its value
# dropdown.is_multiple - This is to check whether the dropdown is multiple or not

# If the dropdowns are dynamic, we have to use the normal Xpath or CSS selectors only to select the dropdown

# 2. Navigate to https://www.globalsqa.com/demo-site/select-dropdown-menu/ and write a code to select 'India' in country dropdown.


from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/home/sacumen/Documents/UdemySelenium/driver/chromedriver")

driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")

dropdown = Select(driver.find_element(By.XPATH,"//select"))
dropdown.select_by_value("IND")

# 3. Navigate to https://www.flipkart.com/ and search 'iphone  14' n search bar,

driver.get("https://www.flipkart.com/")
time.sleep(20)
driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']").click()
print("Closed login form")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@class='_3704LK']").send_keys("iphone  14")
time.sleep(2)
suggested_list = driver.find_elements(By.XPATH, "//li[@class='Y5N33s']/div")

for list in suggested_list:
#a. Print suggested products.
    print("Auto - suggestive options are :", list.text)
#b. Check 'iphone  14 pro' in suggested products and click on it.
    if list.text in 'iphone 14 pro':
        print("Clicking on iphone 14 pro")
        list.click()
        break
#4. Navigate to https://www.flipkart.com/ and click on 'Mobiles' category.
driver.get("https://www.flipkart.com/")

driver.find_element(By.XPATH, "//input[@class='_3704LK']").send_keys("mobiles")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(20)

#    a. Search 'APPLE' in Brand filter
driver.find_element(By.XPATH, "//input[@class='_34uFYj']").send_keys("APPLE")



#    b. Click on APPLE checkbox

driver.find_element(By.XPATH,"//*[@class='_4921Z t0pPfW']").click()
time.sleep(5)

#    c. Then take screenshot.

driver.get_screenshot_as_file("APPLE.png")
# 5. Navigate to https://demoqa.com/radio-button.

driver.get("https://demoqa.com/radio-button")



#    a. Print available radio buttons

ele = driver.find_elements(By.CSS_SELECTOR, ".custom-radio")
count = len(ele)
print("The total number of radio buttons are :", count)
#    b. select 'Yes' radio button

driver.find_element(By.XPATH,"//*[@for='yesRadio']").click()

#    c. Then verify radio button selection

text = driver.find_element(By.CLASS_NAME,"mt-3").text

print(text)

print("------------------------")
# 6. Navigate to 'https://demoqa.com/alerts'

driver.get("https://demoqa.com/alerts")
#    a. Automate 'Click Button to see alert' alert

driver.find_element(By.ID,"alertButton").click()

alert = driver.switch_to.alert

alertText = alert.text

alert.accept()

print(alertText)
print("------------------------")



#    b. Automate 'On button click, alert will appear after 5 seconds' alert

driver.find_element(By.ID,"timerAlertButton").click()

time.sleep(6)

alert1 = driver.switch_to.alert

alertText1 = alert1.text

print(alertText1)

alert1.accept()

print("------------------------")


#    c. Automate 'On button click, confirm box will appear' alert

driver.find_element(By.ID,"confirmButton").click()

alert2 = driver.switch_to.alert

alertText2 = alert2.text

print(alertText2)

alert2.dismiss()

result = driver.find_element(By.ID,"confirmResult").text

print(result)


driver.find_element(By.ID,"confirmButton").click()

alert3 = driver.switch_to.alert

alertText3 = alert3.text

print(alertText3)

alert3.accept()

result1 = driver.find_element(By.ID,"confirmResult").text

print(result1)


print("------------------------")
#    d. Automate 'On button click, prompt box will appear' alert

driver.find_element(By.ID,"promtButton").click()

alert4 = driver.switch_to.alert

alert4.send_keys("Sending alert Text")

alert4.dismiss()

driver.find_element(By.ID,"promtButton").click()

alert5 = driver.switch_to.alert

alert5.send_keys("Sending alert Text Again")

alert5.accept()

result3 = driver.find_element(By.ID,"promptResult").text

print(result3)

print("------------------------")
#
# # 7. What are waits in selenium? Explain difference between them with example.
#
# #Selenium Web Driver Waits are : #


# a.Implicit Wait in Selenium :
# The Implicit Wait in Selenium is used to tell the web driver to wait for a certain amount of time before it throws a “No Such Element Exception”.
# The default setting is 0. Once we set the time, the web driver will wait for the element for that time before throwing an exception.

driver.implicitly_wait(8)
# b.Explicit Wait in Selenium
# The Explicit Wait in Selenium is used to tell the Web Driver to wait for certain conditions (Expected Conditions) or maximum time exceeded before throwing “ElementNotVisibleException” exception.
# It is an intelligent kind of wait, but it can be applied only for specified elements.
# It gives better options than implicit wait as it waits for dynamically loaded Ajax elements.

wait = WebDriverWait(driver,10)

wait.until(expected_conditions.visibility_of_element_located((By.ID,"promptResult")))


# # 8. Prepare basic end to end automation code to add product into cart in flipkart.
# #    Steps to follow
# #    1. Navigate to https://www.flipkart.com/
driver.get("https://www.flipkart.com/")
time.sleep(20)
# #    2. Close the login popup
#Closed already in question 3
# #    3. Search product as mobiles
driver.find_element(By.XPATH, "//input[@class='_3704LK']").send_keys("mobiles")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# #    4. Open first product in list

time.sleep(20)

driver.find_element(By.XPATH,"//*[@class='_1YokD2 _3Mn1Gg']/div[2]/div//a").click()


print("Clicked on the First item of the List")


currentWindow=driver.window_handles
driver.switch_to.window(currentWindow[1])
driver.find_element(By.XPATH,"//*[@class='_2KpZ6l _2U9uOA _3v1-ww']").click()
# #    5. Click on add to cart
print("Clicked on Add to Cart button")

# #    6. then take screenshot.
driver.get_screenshot_as_file("BasketPage.png")

print("Assignment 6 is completed !")






