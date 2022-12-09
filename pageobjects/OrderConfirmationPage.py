import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class OrderConfirmationPage(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    orderNumber = (By.XPATH, "//*[@class='checkout-success']/p[1]")


    def getOrderNumberElement(self):
        return self.driver.find_element(*OrderConfirmationPage.orderNumber)