import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class PaymentPage(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    orderButton = (By.XPATH, "//*[@class='action primary checkout']")


    def getOrderButton(self):
        return self.driver.find_element(*PaymentPage.orderButton)

