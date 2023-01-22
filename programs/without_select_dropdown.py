from asyncio.windows_events import NULL
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


def select_values(options_list,value):

    if not value[0] == 'all':
        for ele in options_list:
        #print(ele.text)

            # if ele.text in value:
            #     ele.click()

            # time.sleep(2)

            
            # if ele.text == value:
            #     ele.click()
            #     time.sleep(2)
            #     break
            for k in range(len(value)):
                if ele.text == value[k] and ele.text != NULL:
                    ele.click()
                    break

            # time.sleep(1)
            # break
    else:
        try:
            for ele in options_list:
                if ele.text != NULL:
                    ele.click()
        except Exception as e:
            print("\nExecption = ",e)


driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.find_element(By.ID,"justAnInputBox").click()
time.sleep(2)

drop_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')


# for ele in drop_list:
#     #print(ele.text)

#     if ele.text == 'choice 2':
#         ele.click()
#     if ele.text == 'choice 2 1':
#         ele.click()
#     if ele.text == 'choice 6 2 3':
#         ele.click()
#         time.sleep(10)
#         break    

list_values = ['all']
select_values(drop_list,list_values)

driver.find_element(By.ID,"justAnInputBox1").click()
time.sleep(2)

drop_list_multiple = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
list_valuess = ['choice 1','choice 2 1', 'choice 6 2 3']
select_values(drop_list_multiple,list_valuess)
