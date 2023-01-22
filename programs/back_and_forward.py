from itertools import dropwhile
from multiprocessing.connection import wait
from select import select
import time
from tkinter import S
from outcome import AlreadyUsedError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# driver = webdriver.Edge(r"D:\\selenium\\msedgedriver.exe")
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)



'''back and forward'''
driver.get("https://amazon.in")
driver.find_element(By.LINK_TEXT,'Best Sellers').click()

driver.back()
driver.forward()
driver.back()

time.sleep(2)

driver.refresh()

time.sleep(2)
