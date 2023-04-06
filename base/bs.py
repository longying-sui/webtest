from selenium.webdriver.common.by import By
from selenium import webdriver

class Base():
    def __init__(self,driver):
        self.driver=driver #type:webdriver

    def fname(self,name):
        return self.driver.find_element(By.NAME, name)

    def fxpath(self,name):
        return self.driver.find_element(By.XPATH, name)

    def open_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()