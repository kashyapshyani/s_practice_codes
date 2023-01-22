import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
#set chromodriver.exe path
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.implicitly_wait(0.5)
#launch URL
driver.get("https://admin-demo.nopcommerce.com/Admin/Discount/Create")

driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()


if not driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card[1]/div/div[2]/div[13]/div[2]/select").is_displayed():
    print("==============\ndisplay elemented\n=================")
    driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/form/section/div/div/div/div/div/div/div/div").click()
else:
    print("============\ndisplay not elemented\n==============")




# ele = driver.find_element(By.CSS_SELECTOR,"label[class=\"onoffswitch-label\"]")
time.sleep(3)

# print("ele ======== \n",ele.value_of_css_property('background-color'))

# print("=====================\n\n\nele text   =======   \n",str(ele))