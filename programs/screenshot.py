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

options = webdriver.EdgeOptions()
options.headless = True
driver = webdriver.Edge(EdgeChromiumDriverManager().install(),options = options)
# driver.maximize_window()
driver.implicitly_wait(10)



'''screenshot'''
driver.get("https://www.reddit.com")
# driver.get_screenshot_as_file("reddit_1.png")

'''fullscreen requires headless mode'''
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('reddit_full_1.png')