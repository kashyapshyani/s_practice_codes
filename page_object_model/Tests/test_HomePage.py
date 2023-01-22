import pytest
from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Test_HomePage(BaseTest):

    elementVisible = (By.XPATH,"/html/body/div[2]/div/div/div/div")
    loginElementVisible = (By.XPATH,"/html/body/div[1]/div/div/div[1]/div/header/div[1]/ul/li[1]/div/div/div/div[2]/div/form/div[1]/div[1]/div[1]")

    def test_home_page_title(self):
        self.homePage = HomePage(self.driver) 
        title = self.homePage.get_title(TestData.FLIPKART_PAGE_TITLE)
        assert title == TestData.FLIPKART_PAGE_TITLE

    # def test_visibility(self):
    #     self.homePage = HomePage(self.driver) 
    #     assert self.homePage.is_visible_element(self.elementVisible)
    
    # def test_go_tologin(self):
    #     self.homePage = HomePage(self.driver) 
    #     self.homePage.go_tologin()
    #     action = ActionChains(self.homePage)
    #     action.move_to_element
    #     assert self.homePage.is_visible_element(self.loginElementVisible)  
    
    # def test_enterSearch(self):
    #      self.homePage = HomePage(self.driver) 
    #      self.homePage.enter_search_text("abc") 

    #flipkart
    # def test_enterCreds(self):
    #     self.homePage = HomePage(self.driver)
    #     self.homePage.do_login_flipkart(TestData.USER_NAME, TestData.PASSWORD)

    def test_ajio_login(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_tologin()
        self.homePage.do_login_ajio(TestData.USER_NAME)

    def test_ajio_signin(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_hoverOnfav("acb")