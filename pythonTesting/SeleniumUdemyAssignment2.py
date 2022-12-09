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

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CSS_SELECTOR,".blinkingText").click()

currentWindow=driver.window_handles
driver.switch_to.window(currentWindow[1])
title = driver.title
assert title == "Rahul Shetty Academy"

print(title)

mailAddress = driver.find_element(By.XPATH,"//p[@class='im-para red']//a").text
assert mailAddress == "mentor@rahulshettyacademy.com"
print(mailAddress)
driver.close()

driver.switch_to.window(currentWindow[0])
title1 = driver.title
assert title1 == "LoginPage Practise | Rahul Shetty Academy"

print(title1)

driver.find_element(By.ID,"username").send_keys("mailAddress")

driver.find_element(By.ID,"password").send_keys("Test1234")

dropdown = Select(driver.find_element(By.XPATH,"//*[@data-style='btn-info']"))
dropdown.select_by_value("teach")



driver.find_element(By.ID,"terms").click()

driver.find_element(By.ID,"signInBtn").click()

wait = WebDriverWait(driver,10)

wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))

print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)