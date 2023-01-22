import pytest
from selenium.webdriver.common.by import By
import time
from pageObjects.LoginPage import LoginPage
from selenium.common.exceptions import NoSuchElementException 
from pageObjects.topics import AddTopic
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random



class Test_020_AddTopic():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def findElement(self):
        try:
            self.driver.find_element_by_css_selector("div[class=\"card card-secondary card-outline collapsed-card\"]").click()
            return True
        except NoSuchElementException:
            return False



    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addTopic(self,setup):
        self.logger.info("************* Test_020_Topic **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Topic Test **********")

        self.addtopic = AddTopic(self.driver)

        self.addtopic.clickOnContentManagement()
        self.addtopic.clickOnTopics()
        self.addtopic.clickOnAddNew()
        if not self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card[3]/div/div[1]").is_displayed():
            self.addtopic.clickOnSlider()
        else:
            pass    
        self.addtopic.setTitle("test title")
        
        # self.addtopic.setBody("test body")

        ans = self.findElement()
        # if ans == True:
            # self.addtopic.clickOnExpandDisply()

        self.addtopic.clickOnPublished()
        self.addtopic.clickOnColumn1()
        self.addtopic.clickOnColumn3()
        # self.addtopic.setCustomerRoles("Vendors")
        self.addtopic.clickUpArrow(5)
        time.sleep(5)
        #self.addtopic.clickOnExpandSEO()
        #self.addtopic.setSearchengine("SEARCH ENGIBBE")
        #self.addtopic.setMakeDescription("dECSRIPTION")
        self.addtopic.clickOnSave()

        self.msg_final = self.driver.find_element(By.CLASS_NAME,"alert-dismissable").text
        self.msg_final = str(self.msg_final)
        # self.logger.info("******* msg final text **********",self.msg_final)
        print("\n\nMessage ====\n\n",self.msg_final)
        if 'For security purposes, the feature you have requested is not available on the demo site.' in self.msg_final:
            assert True
            self.logger.info("********* Add Topic Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addTopic_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False
        
        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")
            

        
