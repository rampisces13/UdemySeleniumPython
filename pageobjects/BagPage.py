import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class BagPage(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    bags = (By.XPATH,"//*[@class='products list items product-items']/li")
    qty = (By.ID, "qty")
    addToCart = (By.ID, "product-addtocart-button")
    cartLink = (By.LINK_TEXT, "shopping cart")



    def getBagElements(self):
        return self.driver.find_elements(*BagPage.bags)

    def getQtyElement(self):
        return self.driver.find_element(*BagPage.qty)

    def getAddToCartElement(self):
        return self.driver.find_element(*BagPage.addToCart)

    def getCartLinkElement(self):
        return self.driver.find_element(*BagPage.cartLink)


    def addBagsToTheCart(self):
        bagsElements = BagPage.getBagElements(self)
        log = self.getLogger()
        for bag in bagsElements:
            bag.find_element(By.XPATH, "div").click()
            log.info("Clicked on the first item")
            break
        BagPage.getQtyElement(self).clear()
        BagPage.getQtyElement(self).send_keys(2)
        BagPage.getAddToCartElement(self).click()
        log.info("Added 2 items to the cart")
        self.driver.implicitly_wait(5)
        BagPage.getCartLinkElement(self).click()
        log.info("Clicked on the shopping cart link")










