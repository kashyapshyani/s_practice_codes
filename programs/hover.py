from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
#set chromodriver.exe path
# driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver = webdriver.ChromeDriver()
driver.implicitly_wait(0.5)
#launch URL
driver.get("https://www.ajio.com/")
#object of ActionChains
a = ActionChains(driver)
#identify element
m = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/header/div[3]/div[2]/div[1]/img")
#hover over element
a.move_to_element(m).perform()
time.sleep(3)
#identify sub menu element
n = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/div/div/div[1]/div/div/div[8]/div/div/a[2]")
# hover over element and click
a.move_to_element(n).click().perform()
print("Page title: " + driver.title)
#close browser
time.sleep(3)
driver.close()