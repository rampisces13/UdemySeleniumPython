# 1. What is pytest and its advantages.
# Pytest is a python based testing framework, which is used to write and execute test codes.
# In the present days of REST services, pytest is mainly used for API testing even though we can use pytest to write simple to complex tests,
# i.e., we can write codes to test API, database, UI, etc.
#
# Advantages of Pytest
# The advantages of Pytest are as follows −
#
# Pytest can run multiple tests in parallel, which reduces the execution time of the test suite.
#
# Pytest has its own way to detect the test file and test functions automatically, if not mentioned explicitly.
#
# Pytest allows us to skip a subset of the tests during execution.
#
# Pytest allows us to run a subset of the entire test suite.
#
# Pytest is free and open source.
#
# Because of its simple syntax, pytest is very easy to start with.
# 2. What are the pre-conditions to created tests in pytest and how to execute in terminal.


# Pre-conditions:
# Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only

# Execution of Pytest in terminal:
# Navigate to the code path in the terminal using CD commands
# ------------------------------------------------------------------------------------------------
# To run all the pytest files execute the command : py.test in the terminal
#
# To have more information on the executed file, run the command py.test - v, where 'v' stands for verbose (more info)
#
# To see all the logs from the pytest, run the command , py.test - v -s , where 's' stands for standard output

#To run only one file , we need to run the command , run the command py.test "filename" - v -s (user has to enter respective filename after py.test)

#To run only specific tests in each file , we need to run the command , run the command py.test -k "keywordofTestcase" - v -s where 'k' stands for keyword expression

#To create a mark(groups in TestNG, tags in cucumber) ,
# add the code "@pytest.mark.smoke" on top of each test cases to make the particular test cases for smoke
#now to run only the marked test cases as "smoke" run the command py.test -m smoke - v -s ,where -m stands for mark

# To Skip a test case, add the code "@pytest.mark.skip", and it will skip the execution
#
# To skip the execution of a test case result in the report, use the command "@pytest.mark.xfail"


# 3. What are fixtures and ther importances in pytest

# Pytest fixtures are functions that can be used to manage our apps states and dependencies.
# Most importantly, they can provide data for testing and a wide range of value types when explicitly called by our testing software.
# You can use the mock data that fixtures create across multiple tests.
#
# Simply, in TestNg, we will have before Test and after test annotations to do certain operations before and after execution of test cases
# eg. launching of browser before execution can be a before Test and closing of browser after the execution is after Test
# in Python we are using fixtures for that

#
# 4.Explain importance of conftest.py file in pytest
#
# When we declare or define something in conftest file, that code will be available for all the pytest test files in the package
#
# we can declare browser invoktion in conftest so that all the test files can have that code
#
# In conftest file, declare a method under fixtures and call the method to any test file using @pytest.mark.usefixtures

# 5. By using page objects in pytest automate following test cases.
#    Test case 1 - launch browser and navigate to "https://magento.softwaretestingboard.com/"

from pageobjects.HomePage import HomePage
from pageobjects.OrderConfirmationPage import OrderConfirmationPage
from pageobjects.PaymentPage import PaymentPage
from utilities.BaseClass import BaseClass
import pytest
from TestData.ShippingPageData import ShippingPageData
from pageobjects.BagPage import BagPage
from pageobjects.CartPage import CartPage
from pageobjects.AddressPage import AddressPage
import time

class TestE2E(BaseClass):
    def test_navigateToHomePage(self,setup):
       homePage = HomePage(self.driver)
       homePage.clickOnBagLink()

#    Test case 2 - Navigate from Gear to Bags and Add product to cart

    def test_addProductsToCart(self):
        bagPage = BagPage(self.driver)
        bagPage.addBagsToTheCart()
#    Test case 3 - Proceed to Checkout and enter all required fields data using data driven fixture
    def test_proceedToCheckout(self):
        cartPage = CartPage(self.driver)
        cartPage.clickOnProceedToCheckout()

    def test_fillShippingDetails(self,getData):
        time.sleep(5)
        addressPage = AddressPage(self.driver)
        addressPage.getEmailElement().send_keys(getData["email"])
        addressPage.getFirstNameElement().send_keys(getData["firstName"])
        addressPage.getLastNameElement().send_keys(getData["LastName"])
        addressPage.getCompanyElement().send_keys(getData["company"])
        addressPage.getStreetLine1Element().send_keys(getData["streetLine1"])
        addressPage.getStreetLine2Element().send_keys(getData["streetLine2"])
        addressPage.getStreetLine3Element().send_keys(getData["streetLine3"])
        addressPage.getCityElement().send_keys(getData["city"])
        self.selectOptionByText(addressPage.getDropDown(),getData["state"])
        addressPage.getPostCodeElement().send_keys(getData["zipCode"])
        addressPage.getTelephoneElement().send_keys(getData["telephone"])
        addressPage.getShippingMethodElement().click()
        addressPage.getNextElement().click()
        log = self.getLogger()
        log.info("Clicked on Next button after entering all the shipping address information")

    #    Test case 4 - Place Order, print the order id

    def test_placeOrder(self):
        time.sleep(5)
        paymentPage = PaymentPage(self.driver)
        paymentPage.getOrderButton().click()
        log = self.getLogger()
        log.info("Clicked on Place order button")

    def test_getOrderID(self):
        order = OrderConfirmationPage(self.driver)
        time.sleep(5)
        orderid = order.getOrderNumberElement().text
        log = self.getLogger()
        log.info(orderid)


#    Test case 5 - In  every test case capture logs and generate HTML report

    @pytest.fixture(params=ShippingPageData.test_ShippingPage_data)
    def getData(self, request):
        return request.param
