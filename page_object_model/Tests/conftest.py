import pytest 
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Config.config import TestData 
# from Config.config import TestData

@pytest.fixture(params=["chrome"], scope='class') 

def init_driver(request): 
    if request.param == "chrome" :
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install()) 
    
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH) 
    
    request.cls.driver = web_driver 
    yield 
    web_driver.close()

