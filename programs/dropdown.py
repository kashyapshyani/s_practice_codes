from itertools import dropwhile
from multiprocessing.connection import wait
from select import select
import time
from tkinter import S
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# driver = webdriver.Edge(r"D:\\selenium\\msedgedriver.exe")
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)




driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/?")

def select_dropdown(element,value):
    select = Select(element)
    select.select_by_visible_text(value)
    time.sleep(3)

ele_country = driver.find_element(By.ID,"Form_submitForm_Country")
ele_state = driver.find_element(By.ID,"Form_submitForm_State")
# select = Select(ele_country)

# select.select_by_visible_text('India')
# time.sleep(2)
# select.select_by_value("Andorra")
# time.sleep(2)

# select.select_by_index(4)
# time.sleep(2)

# print("Is multiple = ",select.is_multiple)

# select.deselect_by_value("India")
# time.sleep(2)
#select_dropdown(ele_country,"India")
#select_dropdown(ele_state,"Gujarat")

select = Select(ele_country)
counrty_list = select.options

for ele in counrty_list:
    # print(ele.text)
    if (ele.text == "I        ndia"):
        select.select_by_visible_text(ele.text)
        ele.click()
        time.sleep(3)
        break