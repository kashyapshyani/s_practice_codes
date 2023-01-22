import time
from selenium.webdriver.common.by import By

class AddTopic:
    lnk_contentManagement = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[6]/a/p"
    lnk_topic = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[6]/ul/li[1]/a/p"
    add_new_button = "/html/body/div[3]/div[1]/div/div/a"
    basic_slider = "/html/body/div[3]/div[1]/form/section/div/div/div/div/div/div/div/div"
    title = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card[1]/div/div[2]/div/div/div[1]/div[2]/input"
    body_textarea = "tinymce"
    customer_roles = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card[2]/div/div[2]/div[9]/div[2]/div/div[1]/div"
    customer_roles_admin = "/html/body/div[4]/div/div[2]/ul/li[1]"
    customer_roles_vendor = "/html/body/div[4]/div/div[2]/ul/li[5]"
    expand_display = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card[2]/div/div[1]/div[2]"
    published_checkbox = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card[2]/div/div[1]/div[2]"
    column_1_checkbox = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card[2]/div/div[2]/div[3]/div[2]/input"
    column_3_checkbox = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card[2]/div/div[2]/div[5]/div[2]/input"
    seo_expand = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card[3]/div/div[1]/div[2]/button/i"
    search_engine_friendly_name = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card[3]/div/div[2]/div/div[1]/div[2]/input"
    make_description = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card[3]/div/div[2]/div/div[4]/div[2]/textarea"
    save_button = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"
    up_arrow = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card[2]/div/div[2]/div[13]/div[2]/span[1]/span/span[2]/span[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnContentManagement(self):
        self.driver.find_element_by_xpath(self.lnk_contentManagement).click()

    def clickOnTopics(self):
        self.driver.find_element_by_xpath(self.lnk_topic).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.add_new_button).click()

    def clickOnSlider(self):
        self.driver.find_element_by_xpath(self.basic_slider).click()

    def setTitle(self,title_1):
        self.driver.find_element_by_xpath(self.title).send_keys(title_1)
        
    def setBody(self,body):    
        self.driver.find_element_by_id(self.body_textarea).send_keys(body)

    def clickOnExpandDisply(self):
        self.driver.find_element_by_xpath(self.expand_display).click()

    def clickOnPublished(self):
        self.driver.find_element_by_xpath(self.published_checkbox).click() 

    def clickOnColumn1(self):
        self.driver.find_element_by_xpath(self.column_1_checkbox).click()    

    def clickOnColumn3(self):
        self.driver.find_element_by_xpath(self.column_3_checkbox).click()    
    
    def clickOnExpandSEO(self):
        self.driver.find_element_by_xpath(self.seo_expand).click()

    def setSearchengine(self,search_engine):
        self.driver.find_element_by_xpath(self.search_engine_friendly_name).send_keys(search_engine)
        
    def setMakeDescription(self,make_description_text):    
        self.driver.find_element_by_xpath(self.make_description).send_keys(make_description_text)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.save_button).click()

    def setCustomerRoles(self,roles):
        self.driver.find_element_by_xpath(self.customer_roles).click()
        time.sleep(3)

        if roles == "Administrators":
            self.listitems = self.driver.find_element_by_xpath(self.customer_roles_admin)
        elif roles == "Vendors":
            self.listitems = self.driver.find_element_by_xpath(self.customer_roles_vendor)
        
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitems)

    def clickUpArrow(self,num):
        for i in range(0,num):
            self.driver.find_element_by_xpath(self.up_arrow).click()

