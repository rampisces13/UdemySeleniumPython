


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#1. Write a python program to
 #   a.launch chrome browser,
  #  b.Navigate to https://sacumen.com/
   # c.Print page title and current url

service_obj = Service("/home/sacumen/Documents/UdemySelenium/driver/chromedriver")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://sacumen.com/")    #Lauching the ChromeBrowser
driver.maximize_window()               #Maximize the Window size
print("The Title of the Page is : " , driver.title)    #Getting the current window's Title
print("The current URL is : ", driver.current_url)     #Getting the current window's URL


print("---------------------------------------------")

# 2. Explain difference between quite() and close() methods.

#The difference between quit() and close()
#driver. quit() : The quit() method quits the driver, closing every associated window.
#driver. close() : The close() method closes the currently focused window, quitting the driver if the current window is the only open window.


# 3. Write a python prgram to launch Opera browser.

# service_obj = Service("/home/sacumen/Documents/UdemySelenium/operadriver/operadriver")#
# driver = webdriver.Opera(service=service_obj)  #
# driver.get("https://sacumen.com/")    #Lauching the OperaBrowser
# driver.maximize_window()

# Note : Selenium is not supporting Opera so commented out the code

# 4. What are Selenium Locators? Explain with syntax.
#
# ID -  Identify the WebElement using the ID attribute - (By.ID,"username")
#
# Name - 	Identify the WebElement using the Name attribute  - driver.find_element(By.NAME ,"loginForm")
#
# ClassName - Use the Class attribute for identifying the object - driver.find_element(By.CLASS_NAME, "form")
#
# LinkText - Use the text in hyperlinks to locate the WebElement - driver.find_element(By.LINK_TEXT, "terms and conditions")
#
# Partial LinkText - Use a part of the text in hyperlinks to locate the desired WebElement - driver.find_element(By.PARTIAL_LINK_TEXT, "terms")
#
# TagName - Use the TagName to locate the desired - driver.find_element(By.TAG_NAME, "a")
#
# CssSelector - CSS used to create style rules in web page is leveraged to locate the desired WebElement - (By.CSS_SELECTOR, ".alert-danger")
#
# XPath - Use XPath to locate the WebElement  - (By.XPATH, "//div[@class='product']")

# 5. Explain difference between css and xpath locators with example.

# Xpath allows bidirectional flow which means the traversal can be both ways from parent to child and child to parent as well. Css allows only one directional flow which means the traversal is from parent to child only.
#
# Xpath is slower in terms of performance and speed. Css has better performance and speed than xpath.
#
# Xpath allows identification with the help of visible text appearing on screen with the help of text() function. Css does not have this feature.
#
# Customized css can be created directly with the help of attributes id and class. For id, the css expression is represented by # followed by the id [ #<<id expression>>. For class, the css expression is represented by . followed by the class [.<<class expression>>]. Xpath does not have any feature like this.
#
# Xpath expression is represented by [//tagname[@attribute = 'value']. The css expression is repression is represented by [tagname[attribute = 'value'].
#
# There are two types of xpath – absolute and relative. But css has no such types.


driver.get("https://rahulshettyacademy.com/loginpagePractise/")    #Lauching the ChromeBrowser
driver.maximize_window()               #Maximize the Window size

# Xpath to locate the User name field in the mentioned website is

driver.find_element(By.XPATH,"//*[@id = 'username']").send_keys("Ramkumar")
driver.find_element(By.XPATH,"//*[@id = 'username']").clear()

# CSS to locate the User name field in the mentioned website is
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("Ram")

# 6. Explain click() and send_keys() methods in selenium with example.

#sendkeys() in Selenium is a method used to enter editable content in the text and password fields during test execution.
# These fields are identified using locators like name, class, id, etc. It is a method available on the web element.
#sendkeys() method does not replace existing text in any text box.

#Example

driver.find_element(By.NAME,"password").send_keys("Test")


#The Selenium click buttons can be accessed using the click() method.

#Example

driver.find_element(By.ID,"signInBtn").click()

wait = WebDriverWait(driver,10)

wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))

print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

print("---------------------------------------------")

# 7. Explain Tag names and attributes in HTML.

#Tag names :
#A tag name is a part of a DOM structure where every element on a page is been defined via tag like input tag, button tag or anchor tag etc.
# Each tag has multiple attributes like ID, name, value class etc. As far as other locators in Selenium are concerned, we used these attributes values of the tag to locate elements.
# In the case of tag name Selenium locator, we will simply use the tag name to identify an element.

#Example :
#Email Field: < input type="email" name="email" value="" placeholder="Email" required="required" autofocus="autofocus" class="form-control mt-3 form-control-lg">

# In the above example, Input is the tage name which represents the field is expecting some inputs

# Commonly used Tagnames in selenium are :
# a - for hyperlink
# div - The div tag is known as Division tag. The div tag is used in HTML to make divisions of content in the web page like (text, images, header, footer, navigation bar, etc)
# h1 - For headers
# td - table
# tr - table row
# p - for paragraph
# style - for css styling
# iframe - for the iFrame
#button - for the button
#label - for the Label
#select - For Select class

#Attributes:
# Attributes are additional bits of information developers include in HTML tags.
# Attributes help in defining the characteristics of HTML elements.

# Commonly used attributes in selenium are :

#id
#name
#class
#type
#value
#for

#The getAttribute() Method
# The getAttribute() method fetches the text contained by an attribute in an HTML document.
# It returns the value of the HTML element's attribute as a string.
# If a value is not set for an attribute, it will return a NULL value.
# For attributes with Boolean values, getAttribute() will return either "True" or NULL.

a = driver.find_element(By.ID,'signInBtn').get_attribute("value")
print(a)
assert a == "Sign In"

print("---------------------------------------------")

print("Assignment 5 is completed !")

print("---------------------------------------------")