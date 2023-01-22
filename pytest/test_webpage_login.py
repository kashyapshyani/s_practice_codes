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
# driver = webdriver.Edge(r"D:\\selenium\\msedgedriver.exe")
# driver = webdriver.Edge(EdgeChromiumDriverManager().install())
# driver.maximize_window()
# driver.implicitly_wait(10)

# driver.get("https://www.spicejet.com")
# time.sleep(3)


# '''move to element'''

# add_on_ele = driver.find_element_
# act_chains = ActionChains(driver)
# act_chains.move_to_element(add_on_ele).perform()
# time.sleep(2)

'''drag and drop'''
# driver.get('https://jqueryui.com/resources/demos/droppable/default.html')

# source = driver.find_element(By.ID, 'draggable')
# target = driver.find_element(By.ID, 'droppable')

# act_chains = ActionChains(driver)
# act_chains.drag_and_drop(source,target).perform()

# time.sleep(2)

# driver.get('https://jqueryui.com/resources/demos/droppable/default.html')

# source = driver.find_element(By.ID, 'draggable')
# target = driver.find_element(By.ID, 'droppable')

# act_chains = ActionChains(driver)
# act_chains.click_and_hold(source).move_to_element(target).release().perform()

# time.sleep(2)

'''right click'''

# driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')

# right_click_ele = driver.find_element(By.XPATH,"//span[text()='right click me']")
# act_chains = ActionChains(driver)
# act_chains.context_click(right_click_ele).perform()

# right_click_options = driver.find_elements(By.CSS_SELECTOR, 'li.context-menu-icon span')
# for ele in right_click_options:
#     print(ele.text)
#     if ele.text == 'Copy':
#         ele.click()
#         break

'''series of actions'''

def test_google():

    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://classic.crmpro.com')
    assert driver.title != "Google"
    time.sleep(3)


    # username_ele =  driver.find_element(By.NAME,"username")
    # password_ele =  driver.find_element(By.NAME,"password")
    # login_button = driver.find_element(By.XPATH, "//input[@type='submit']")

    # act_actions = ActionChains(driver)
    # act_actions.send_keys_to_element(username_ele,'abc').perform()
    # act_actions.send_keys_to_element(password_ele,'abc').perform()
    # act_actions.click(login_button).perform()

    # time.sleep(2)

    driver.quit()

def test_facebook():

    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.facebook.com')
    assert driver.title != "Google"
    time.sleep(3)


    # username_ele =  driver.find_element(By.NAME,"username")
    # password_ele =  driver.find_element(By.NAME,"password")
    # login_button = driver.find_element(By.XPATH, "//input[@type='submit']")

    # act_actions = ActionChains(driver)
    # act_actions.send_keys_to_element(username_ele,'abc').perform()
    # act_actions.send_keys_to_element(password_ele,'abc').perform()
    # act_actions.click(login_button).perform()

    # time.sleep(2)

    driver.quit()   

def test_gamil():

    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.gmail.com')
    assert driver.title != "Gmail"
    time.sleep(3)


    # username_ele =  driver.find_element(By.NAME,"username")
    # password_ele =  driver.find_element(By.NAME,"password")
    # login_button = driver.find_element(By.XPATH, "//input[@type='submit']")

    # act_actions = ActionChains(driver)
    # act_actions.send_keys_to_element(username_ele,'abc').perform()
    # act_actions.send_keys_to_element(password_ele,'abc').perform()
    # act_actions.click(login_button).perform()

    # time.sleep(2)

    driver.quit()   


#run with command - py.test -n 3 -v
