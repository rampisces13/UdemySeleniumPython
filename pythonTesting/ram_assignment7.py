# 1. Explain few methods in ActionChains with sample code.
#
# ActionChains are a way to automate low-level interactions such as mouse movements, mouse button actions, keypress, and context menu interactions.
#
# This is useful for doing more complex actions like hover over and drag and drop. Action chain methods are used by advanced scripts where we need to drag an element, click an element
#
# ActionChains are implemented with the help of a action chain object which stores the actions in a queue and when perform() is called, performs the queued operations.
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/home/sacumen/Documents/UdemySelenium/driver/chromedriver")

driver = webdriver.Chrome(service=service_obj)

# get geeksforgeeks.org
driver.get("https://sacumen.com/")

driver.maximize_window()

# create action chain object
action = ActionChains(driver)

element = driver.find_element(By.CLASS_NAME,"hamburger-321")

action.move_to_element(element).perform()

action.click(element).perform()

print("-------------------------------------------")

# 2. Write a python code by covering below points
#    a. Navigate to "https://magento.softwaretestingboard.com/"
driver.get("https://magento.softwaretestingboard.com/")
driver.implicitly_wait(2)

#    b. Using Actionchains method navigate to Gear -> Watches

gearElement = driver.find_element(By.ID,"ui-id-6")

action.move_to_element(gearElement).perform()

watchElement =  driver.find_element(By.ID,"ui-id-27")

action.move_to_element(watchElement).perform()

action.click(watchElement).perform()

#    c. Add product names into list and print it

watchList = []
driver.implicitly_wait(2)

watches = driver.find_elements(By.XPATH,"//*[@class='products list items product-items']/li")

for watch in watches:
    watchText = watch.find_element(By.XPATH,"div/div//a").text
    print(watchText)
    watchList.append(watchText)

print(watchList)

print("-------------------------------------------")

# 3. Write a python code by covering below points
#    a. Navigate to "https://nxtgenaiacademy.com/multiplewindows/"
driver.get("https://nxtgenaiacademy.com/multiplewindows/")

#    b. Click on 'New Browser Window' button. Maximize newly opened window, print the page tile and close new window. Finally get back to old window.
browserButton = driver.find_element(By.XPATH,"//*[@name='newbrowserwindow123']")
browserOldTitle = driver.title
print("The Parent window Tile is :" ,browserOldTitle)
action.move_to_element(browserButton).perform()
action.click(browserButton).perform()
currentWindow=driver.window_handles
driver.switch_to.window(currentWindow[1])
driver.maximize_window()
browserNewTitle = driver.title
print("The new window Tile is :" ,browserNewTitle)
driver.close()
driver.switch_to.window(currentWindow[0])
currentTitle = driver.title
assert currentTitle == browserOldTitle
print("-------------------------------------------")



#    c. Click on 'New Browser Tab' button. Print the page tile of new tab and close the new tab. Finally get back to old tab.
browserTab = driver.find_element(By.XPATH,"//*[@name='newbrowsertab453']")
windowOldTitle = driver.title
print("The Parent window Tile is :" ,windowOldTitle)
action.move_to_element(browserTab).perform()
action.click(browserTab).perform()
currentWindow=driver.window_handles
driver.switch_to.window(currentWindow[1])
driver.maximize_window()
windowNewTitle = driver.title
print("The new window Tile is :" ,windowNewTitle)
driver.close()
driver.switch_to.window(currentWindow[0])
currentTitle1 = driver.title
assert currentTitle1 == windowOldTitle
print("-------------------------------------------")

# 4. Write a python code by covering below points
#    a. Navigate to "https://the-internet.herokuapp.com/frames"
driver.get("https://the-internet.herokuapp.com/frames")
#    b. Click on iFrame
driver.find_element(By.LINK_TEXT,"iFrame").click()
#    c. Print available text in input field and clear it
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
#    d. Enter "Automation engineer at Sacumen" in input
driver.find_element(By.ID,"tinymce").send_keys("Automation engineer at Sacumen")
#    e. After entering text, take screenshot
driver.get_screenshot_as_file("frame.png")
driver.switch_to.default_content()
print("Question 4 is completed")
print("-------------------------------------------")

# 5. Automate Place Order feature in "https://magento.softwaretestingboard.com/", consider below steps.
#
# a.Navigate to "https://magento.softwaretestingboard.com/"

driver.get("https://magento.softwaretestingboard.com/")
driver.implicitly_wait(5)

# b.Navigate to  Gear -> Bags
gearElement1 = driver.find_element(By.ID,"ui-id-6")
action.move_to_element(gearElement1).perform()

BagElement =  driver.find_element(By.ID,"ui-id-25")

action.move_to_element(BagElement).perform()

action.click(BagElement).perform()

# c.Click on  any product
driver.implicitly_wait(2)

bags = driver.find_elements(By.XPATH,"//*[@class='products list items product-items']/li")

for bag in bags:
    bag.find_element(By.XPATH,"div").click()
    print("Clicked on the first item")
    break

# d. Add qty as "2" then click on 'Add to Cart'
driver.find_element(By.ID,"qty").clear()
driver.find_element(By.ID,"qty").send_keys(2)
driver.find_element(By.ID,"product-addtocart-button").click()
print("Clicked on Add to card button")
# e. Then click on "shopping cart." link
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"shopping cart").click()
# f. Click on 'Proceed to Checkout' button
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//*[@data-role='proceed-to-checkout']").click()
# g. Enter all the required fields
driver.implicitly_wait(2)
# h. Click "on Next"
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.ID,"customer-email")))
driver.find_element(By.ID,"customer-email").send_keys("123@abc.com")
driver.find_element(By.XPATH,"//*[@name='firstname']").send_keys("Test FirstName")
driver.find_element(By.XPATH,"//*[@name='lastname']").send_keys("Test LastName")
driver.find_element(By.XPATH,"//*[@name='company']").send_keys("Test Company")
driver.find_element(By.XPATH,"//*[@name='street[0]']").send_keys("Street Line 1")
driver.find_element(By.XPATH,"//*[@name='street[1]']").send_keys("Street Line 2")
driver.find_element(By.XPATH,"//*[@name='street[2]']").send_keys("Street Line 3")
driver.find_element(By.XPATH,"//*[@name='city']").send_keys("City Name")

dropdown = Select(driver.find_element(By.XPATH,"//*[@name='region_id']"))
dropdown.select_by_value("47")

driver.find_element(By.XPATH,"//*[@name='postcode']").send_keys("45011")
driver.find_element(By.XPATH,"//*[@name='telephone']").send_keys("1234567890")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//*[@name='ko_unique_4']").click()
driver.find_element(By.XPATH,"//*[@class='button action continue primary']").click()

# i. Click on "Place Order"
time.sleep(5)
driver.find_element(By.XPATH,"//*[@class='action primary checkout']").click()

# j. Print order number and take screenshot
driver.implicitly_wait(5)
ordernumber = driver.find_element(By.XPATH,"//*[@class='checkout-success']/p[1]").text
print(ordernumber)

driver.get_screenshot_as_file("order.png")

print ("------------------------------------------------------------------")

print("Assignment 7 is completed !")
