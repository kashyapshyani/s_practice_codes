import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchOrdersPage import SearchOrdersPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_SearchOrders:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_searchOrdersInPage(self,setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.searchOrders = SearchOrdersPage(self.driver) 
        self.searchOrders.click_on_sales()
        self.searchOrders.click_on_orders()       
        self.searchOrders.click_on_billing_country_dropdown(10)
