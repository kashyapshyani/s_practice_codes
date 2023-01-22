import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# driver = webdriver.Edge(r"D:\\selenium\\msedgedriver.exe")
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.maximize_window()
# driver.implicitly_wait(10)

url = "https://3e8e4a48beac473b911000414820d91a.us-central1.gcp.cloud.es.io:9243/app/kibana#/dashboard/azure_metrics-b165ef60-32f7-11ea-a83e-25b8612d00cc"

email = "herop81846@cosaxu.com"
password = "Herop1846@"

ll = ["Availability","Egress Traffic by APIName","Storage filters [Azure Metrics]"]

login_with_cloud = "/html/body/div[1]/div[3]/div[2]/div/div/div/div/div[1]/button[2]/div/div[2]/p[1]"
email_field = "email"
password_field = "password"
login_button = "//*[@id=\"app-root\"]/div[1]/div[3]/div/div[2]/form/div[3]/button"
main_parent_div = "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]/div"

                #    /html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/figcaption/h2/span[2]/span

try_e = "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/figcaption/h2/span[2]/span"
try_x ="/html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div"

driver.get(url)


ele = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, login_with_cloud)))
ele.click()
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, email_field))).send_keys(email)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, password_field))).send_keys(password)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, login_button))).click()
# WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, main_parent_div)))
time.sleep(60)
ele = WebDriverWait(driver, 25).until(EC.visibility_of_any_elements_located((By.XPATH, main_parent_div)))

new_l = []

for i in range(11):
    n = i+1
    new_p = main_parent_div + "/div["+str(n)+"]/div/div/figcaption/h2/span[2]/span"
    # e1 = WebDriverWait(driver, 25).until(EC.element_to_be_selected((By.XPATH, new_p)))
    e1 = driver.find_element(By.XPATH,new_p)
    print("==============================\ne1 = ",e1.text)
    new_l.append(e1.text)


print("==============================\nterxt = ",new_l)

count=0
for i in ll:
    if i in new_l:
        count=0
        continue
    else:
        print("fail\nele = ",i)
        count=1
        break

if count==0:
    print("pass")



# print("\n\n\n===============================")
# new_l = []

# for i in ele:
#     print(i.text)
#     new_l.append(i.text)

# print("\n\n\n===============================new_l = ",len(ele))


# print("\n\n\n===============================new list=====\n")
# for i in new_l:
#     print(i)

# for i in ll:
#     if i in new_l:
#         continue
#     else:
#         print("\n\n\n===============================FAIL")
#         break

# print("\n\n\n===============================PASS")