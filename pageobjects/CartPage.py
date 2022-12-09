import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class CartPage(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    checkoutButton = (By.XPATH,"//*[@data-role='proceed-to-checkout']")

    def getCheckoutButtonElement(self):
        return self.driver.find_element(*CartPage.checkoutButton)

    def clickOnProceedToCheckout(self):
        self.driver.implicitly_wait(5)
        CartPage.getCheckoutButtonElement(self).click()
        log = self.getLogger()
        log.info("Clicked on Proceed to Checkout button")
