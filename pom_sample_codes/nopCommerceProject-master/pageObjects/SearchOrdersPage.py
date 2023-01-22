import time
from selenium.webdriver.support.ui import Select

class SearchOrdersPage:
    clickOnSales = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/a/p"
    clickOnOrders = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li[1]/a"
    startDate_calender = "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[2]/span/span/span"
    endDate_calender = "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[2]/span/span/span"

    billing_country = "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div[6]/div[2]/select"
    payment_method = "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div[7]/div[2]/select"


    def __init__(self, driver):
        self.driver = driver

    def click_on_sales(self):
        self.driver.find_element_by_xpath(self.clickOnSales).click()

    def click_on_orders(self):
        self.driver.find_element_by_xpath(self.clickOnOrders).click()

    def click_on_billing_country_dropdown(self,country):
        self.driver.find_element_by_xpath(self.billing_country).click()
        time.sleep(1)
        ele = self.driver.find_element_by_xpath(self.billing_country)
        ele.select_by_index(country)
        time.sleep(1)