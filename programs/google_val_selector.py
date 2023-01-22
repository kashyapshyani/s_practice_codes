import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com")

driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("real madrid")


# searchText_google_suggestion = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div/ul/li/div/div[2]/div[1]/span")))
searchText_google_suggestion = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//li[class=\"sbct\"]/div/div[2]/div[1]/span")))

for item in searchText_google_suggestion :
    print(item.text)