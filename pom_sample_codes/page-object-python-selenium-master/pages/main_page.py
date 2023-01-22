from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignUpBasePage
from utils.locators import *
from selenium.webdriver.common.action_chains import ActionChains
import time



# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def search_item(self, item):
        self.find_element(*self.locator.SEARCH).send_keys(item)
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        return self.find_element(*self.locator.SEARCH_LIST).text

    def click_sign_up_button(self):
        self.find_element(*self.locator.SIGNUP).click()
        return SignUpBasePage(self.driver)

    def click_sign_in_button(self):
        self.find_element(*self.locator.LOGIN).click()
        return LoginPage(self.driver)

    def do_hover_action(self):
        a = ActionChains(self.driver)
        m = self.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]")
        a.move_to_element(m).perform()
        n = self.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div[3]/div[2]/div/div[2]/a[3]")
        a.move_to_element(n).click().perform()
        time.sleep(5)

    def do_navigation_sidebar(self):
        self.find_element(By.XPATH,"/html/body/div[1]/header/div/div[4]/div[1]").click()
        time.sleep(1)
        self.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/ul[1]/li[8]/a").click()
        time.sleep(1)
        self.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/ul[6]/li[17]/a").click()
        time.sleep(1)
        ele = self.find_element(By.CLASS_NAME,"puis-padding-right-small")
        ele.select_by_index(2)
        time.sleep(1)
        print("ele =====\n",ele.text)