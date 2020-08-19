from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

PATH = 'C:\Program Files (x86)/chromedriver.exe'

class InstagramBot :

    def __init__(self, username, password):
        self.username= username
        self.password = password

        self.driver= webdriver.Chrome(PATH)

        self.login()

    def login(self):
        self.driver.get('http://www.instagram.com/')
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_name('username').send_keys(self.username)
        

        self.driver.find_element_by_name('password').send_keys(self.password)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()

if __name__ == '__main__' :
    ig_bot = InstagramBot('georgepovoa12@gmail.com', 'asdasd12')

    print(ig_bot.username)
