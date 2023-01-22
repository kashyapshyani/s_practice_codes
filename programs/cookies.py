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



'''cookies'''
driver.get("https://reddit.com")

# cookies = driver.get_cookies()

# for cook in cookies:
#     print(cook)

print(driver.get_cookies())

driver.add_cookie({"name":"abc","domain":"reddit.com","value":"abc"})

cookies = driver.get_cookies()

print("\n\n\n")

for cook in cookies:
    print(cook)