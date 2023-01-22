from argparse import Action
from asyncio.windows_events import NULL
from itertools import dropwhile
from multiprocessing.connection import wait
from select import select
import time
from turtle import right
from selenium.webdriver import ActionChains
from tkinter import S
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest

driver = None

def setup_module(module):
    global driver
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://google.com')

def teardown_module():
    driver.quit()

def test_google_title():
    assert driver.title == 'Google'

def test_google_url():
    assert driver.current_url == 'google.com'   




#run with -  py.test -v -s .\test_google_test_xe.py  --html=google_report_test.html