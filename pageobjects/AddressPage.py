import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self,driver):
        self.driver = driver

    emailAddress = (By.ID,"customer-email")
    firstName = (By.XPATH, "//*[@name='firstname']")
    lastName = (By.XPATH, "//*[@name='lastname']")
    company = (By.XPATH, "//*[@name='company']")
    streetLine1 = (By.XPATH, "//*[@name='street[0]']")
    streetLine2 = (By.XPATH, "//*[@name='street[1]']")
    streetLine3 = (By.XPATH, "//*[@name='street[2]']")
    city = (By.XPATH, "//*[@name='city']")
    postCode= (By.XPATH, "//*[@name='postcode']")
    telePhone = (By.XPATH, "//*[@name='telephone']")
    shippingMethod = (By.XPATH, "//*[@name='ko_unique_4']")
    nextButton = (By.XPATH, "//*[@class='button action continue primary']")
    dropdown = (By.XPATH, "//*[@name='region_id']")

    def getEmailElement(self):
        return self.driver.find_element(*AddressPage.emailAddress)

    def getFirstNameElement(self):
        return self.driver.find_element(*AddressPage.firstName)

    def getLastNameElement(self):
        return self.driver.find_element(*AddressPage.lastName)

    def getCompanyElement(self):
        return self.driver.find_element(*AddressPage.company)

    def getStreetLine1Element(self):
        return self.driver.find_element(*AddressPage.streetLine1)

    def getStreetLine2Element(self):
        return self.driver.find_element(*AddressPage.streetLine2)

    def getStreetLine3Element(self):
        return self.driver.find_element(*AddressPage.streetLine3)

    def getCityElement(self):
        return self.driver.find_element(*AddressPage.city)

    def getPostCodeElement(self):
        return self.driver.find_element(*AddressPage.postCode)

    def getTelephoneElement(self):
        return self.driver.find_element(*AddressPage.telePhone)

    def getShippingMethodElement(self):

        return self.driver.find_element(*AddressPage.shippingMethod)

    def getNextElement(self):
        return self.driver.find_element(*AddressPage.nextButton)

    def getDropDown(self):
        return self.driver.find_element(*AddressPage.dropdown)

