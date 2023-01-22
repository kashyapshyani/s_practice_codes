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
from webdriver_manager.firefox import GeckoDriverManager

import pytest

@pytest.fixture(params=["chrome","firefox"],scope='class')
def init_driver(request):
    if request.param == "chrome":
        print("==========================setup=======================")
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    if request.param == "firefox":
        print("==========================setup=======================")
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = web_driver

    yield
    print("==========================tear down=======================")
    web_driver.close()
