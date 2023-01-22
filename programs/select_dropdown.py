import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# import timedriver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.implicitly_wait(0.5)
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
# identify dropdown with Select class
sel = Select(driver.find_element_by_xpath("//select[@name='continents']"))
#select by select_by_visible_text() method
sel.select_by_visible_text("Europe")
time.sleep(5)
#select by select_by_index() method
sel.select_by_index(0)

drop_list = driver.find_elements(By.XPATH, "//select[@name='continents']")
for ele in drop_list:
    print(ele.text)

    if ele.text == 'Africa':
        ele.click()
        break
    # if ele.text == 'choice 2 1':
    #     ele.click()
    # if ele.text == 'choice 6 2 3':
    #     ele.click()
    #     time.sleep(10)
    #     break    
time.sleep(5)


driver.close()