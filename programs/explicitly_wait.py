from asyncio import sleep
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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# driver = webdriver.Edge(r"D:\\selenium\\msedgedriver.exe")

options = webdriver.EdgeOptions()
options.headless = True
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
# driver.maximize_window()
# driver.implicitly_wait(10)



'''explicitly wait'''
# driver.get("https://app.hubspot.com/login")
# wait = WebDriverWait(driver,10)

# # wait.until(ec.title_is('HubSpot Login'))
# wait.until(ec.title_contains('HubSpot'))


# print("page title = ",driver.title)

'''explicilty wait alert'''
# driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
# driver.find_element(By.NAME,'proceed').click()

# wait = WebDriverWait(driver,10)

# alert = wait.until(ec.alert_is_present())

# print(alert.text)
# alert.accept()
# driver.close()

'''explicitly sign up visible'''
# driver.get("https://app.hubspot.com/login")
# # driver.find_element(By.NAME,'proceed').click()

# wait = WebDriverWait(driver,10)

# sign_up_link  = wait.until(ec.element_to_be_clickable((By.LINK_TEXT,'Sign up')))
# print(sign_up_link.text)
# sign_up_link.click()

# first_name = wait.until(ec.visibility_of_element_located((By.NAME,'FIRST_NAME')))
# first_name.send_keys('abc')

'''explicitly all element located'''
driver.get("https://www.freshworks.com")

wait = WebDriverWait(driver,10)
footer_links = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.footer-nav li')))
print(len(footer_links))

for ele in footer_links:
    print(ele.text)

wait.until(ec.frame_to_be_available_and_switch_to_it((By.ID,'test')))    
wait.until(ec.element_located_to_be_selected('checkbox'))
wait.until(ec.url_contains('freshworks'))
time.sleep(3)