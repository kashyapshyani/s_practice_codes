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



'''alert pop up'''
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")


driver.find_element(By.CLASS_NAME,"signinbtn").click()

alert_ref = driver.switch_to.alert
print("alert text = ",alert_ref.text )
alert_ref.accept()

time.sleep(2)

driver.switch_to.default_content()

driver.find_element(By.CLASS_NAME,"signinbtn").click()

alert_ref = driver.switch_to.alert
print("alert text = ",alert_ref.text )
alert_ref.accept()

time.sleep(2)

driver.switch_to.default_content()

'''frame'''
# driver.get("http://londonfreelance.org/courses/frames/index.html")
# #driver.switch_to.frame(2)
# #driver.switch_to.frame('main')

# frame_element = driver.find_element(By.NAME,"main")
# driver.switch_to.frame(frame_element)

# headerValue = driver.find_element(By.CSS_SELECTOR,"body > h2").text
# print("header value = ",headerValue) 


'''authentication pop up '''

# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")


# time.sleep(2)

'''file_upload'''

# driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")
# driver.find_element(By.NAME,'upfile').send_keys('F:\\Users\\Administrator\\Desktop\\file.txt')

# time.sleep(2)

# driver.find_element(By.XPATH,"/html/body/form/input[3]").click()
# time.sleep(3)