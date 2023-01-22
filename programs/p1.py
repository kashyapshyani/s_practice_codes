from multiprocessing.connection import wait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# driver = webdriver.Edge(r"D:\\selenium\\msedgedriver.exe")
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.implicitly_wait(5)


driver.get("https://www.google.com")
driver.find_element(By.NAME,"q").send_keys("hello")
optionList = driver.find_elements(By.CSS_SELECTOR,"ul.erkvQe li span")
print(optionList)

for ele in optionList:
    print(ele.text)
    if ele.text == 'Hello Hello!':
        ele.click()
        break
    

time.sleep(5)

# print(driver.title)
driver.quit()