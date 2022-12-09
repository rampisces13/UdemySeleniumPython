import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/home/sacumen/Documents/UdemySelenium/driver/chromedriver")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

vegActualList = []
vegExpectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']

productLists = driver.find_elements(By.XPATH, "//div[@class='product']")

for productList in productLists:
    productName = productList.find_element(By.XPATH,"h4").text
    vegActualList.append(productName)
    productList.find_element(By.XPATH,"div[3]/button").click()
    print("Clicked on the Add to Cart Button")

print(vegActualList)
assert vegActualList == vegExpectedList

Items = int(driver.find_element(By.XPATH, "//tr/td[3]").text)

assert Items == 3

driver.find_element(By.CLASS_NAME, "cart-icon").click()

driver.find_element(By.CSS_SELECTOR, ".action-block").click()
print("Clicked on the Proceed To Checkout Button")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

promoText = driver.find_element(By.CSS_SELECTOR,".promoInfo").text

assert promoText == "Code applied ..!"

prices = driver.find_elements(By.XPATH,"//tbody/tr/td[5]")
sum = 0

for price in prices:
    sum = sum+ int(price.text)


print(sum)


totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert totalAmount == sum

print("The Total Amount is :", totalAmount)

discountPercentage = driver.find_element(By.CSS_SELECTOR, ".discountPerc").text


assert discountPercentage == "10%"

discountedPrice= totalAmount * 10 / 100

print("The Discounted Price is :", discountedPrice)

finalPrice = totalAmount - discountedPrice

totalAfterDiscount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert totalAfterDiscount == finalPrice

print("The Final Price is :", finalPrice)