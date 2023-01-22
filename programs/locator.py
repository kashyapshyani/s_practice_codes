from itertools import dropwhile
from multiprocessing.connection import wait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# driver = webdriver.Edge(r"D:\\selenium\\msedgedriver.exe")
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)


# driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/?")
#driver.get("https://app.hubspot.com/login")
#time.sleep(5)
#driver.find_element(By.CSS_SELECTOR,"input.form-control.private-form__control.login-email").send_keys("445")
#driver.find_element(By.CSS_SELECTOR,"input.form-control.private-form__control.login-password.m-bottom-3").send_keys("123")
#driver.find_element(By.LINK_TEXT,"Sign up").click()

#time.sleep(5)

#tagname
driver.get("https://www.amazon.in/")


# header_list = driver.find_elements(By.TAG_NAME,"a")
# #print("Headers==========\n",header.text)

# for ele in header_list:
#     ele_text = ele.text
#     print(ele_text)
#     print(ele.get_attribute('href'))
#     if (ele.get_attribute('href')=="https://www.amazon.in/gp/help/customer/display.html?nodeId=200545940&ref_=footer_cou"):
#         print("found")
#         break

image_list = driver.find_elements(By.TAG_NAME,"img")
#print("Headers==========\n",header.text)

for ele in image_list:
    ele_text = ele.text
    print(ele_text)
    print(ele.get_attribute('src'))
    
