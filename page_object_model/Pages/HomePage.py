from selenium.webdriver.common.by import By
from Config.config import TestData
from selenium import webdriver
import time
from Pages.BasePage import BasePage

class HomePage(BasePage):
    loginTxt = (By.XPATH,"/html/body/div/div/div/div[1]/div/header/div[1]/ul/li[1]/span")
    loginPopUP = (By.CLASS_NAME,"_3wFoIb row")
    modalLoginContainer = (By.CLASS_NAME,"modal-login-container")
    elementVisible = (By.CLASS_NAME,"img-animate")
    searchBar = (By.NAME,"searchVal")
    EMAIL = (By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
    PASSWORD = (By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
    LOGIN_BUTTON = (By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button")
    clickSearch = (By.CLASS_NAME, "ic-search")
    EMAIL_ajio = (By.NAME,"username")
    Login_button_ajio = (By.CLASS_NAME,"login-btn")
    fav_button_ajio = (By.XPATH,"/html/body/div/div/div/div[1]/div/header/div[3]/div[2]/div[1]")

    '''constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.FLIPKART_BASE_URL)

    '''this is used to get the page title''' 
    def get_home_page_title(self, title):
        return self.get_title(title)

    '''this is used to login to app''' 
    def go_tologin(self): 
        self.do_click(self.loginTxt)  

    def is_visible_element(self,element):
        return self.is_visible(element)      

    def enter_search_text(self,text):
        self.do_send_keys(self.searchBar, text)
        self.do_click(self.clickSearch)
        time.sleep(5)
    
    def do_login_flipkart(self, username, password):
        self.do_send_keys(self.EMAIL, username) 
        self.do_send_keys(self.PASSWORD, password) 
        self.do_click(self.LOGIN_BUTTON)

    def do_login_ajio(self, username):
        self.do_send_keys(self.EMAIL_ajio, username) 
        # self.do_send_keys(self.PASSWORD, password) 
        self.do_click(self.Login_button_ajio)
        time.sleep(5)
    
    def do_hoverOnfav(self,ele):
        # self.hover(self.fav_button_ajio)
        abc = ele
        self.do_click(self.fav_button_ajio)
        time.sleep(5)