import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class HomePage(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    gear = (By.ID, "ui-id-6")
    bag = (By.ID, "ui-id-25")


    def clickOnBagLink(self):
        self.driver.implicitly_wait(2)
        action = ActionChains(self.driver)
        action.move_to_element(HomePage.getGearElement(self)).perform()
        action.move_to_element(HomePage.getBagElement(self)).perform()
        action.click(HomePage.getBagElement(self)).perform()
        log = self.getLogger()
        log.info("Clicked on Bag link")



    def getGearElement(self):
        return self.driver.find_element(*HomePage.gear)

    def getBagElement(self):
        return self.driver.find_element(*HomePage.bag)



