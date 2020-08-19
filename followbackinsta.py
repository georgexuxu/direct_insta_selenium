from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
#login
username = 'wikibotgx'
password = 'Asdasdig12.'
#configure chrome to open on mobile mode for exclusive features
mobile_emulation = { "deviceName": 'iPhone 5' }
opts = webdriver.ChromeOptions()
opts.add_experimental_option("mobileEmulation", mobile_emulation)
#open browser
driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)/chromedriver.exe",options=opts) #you must enter the path to your driver
actionChains = ActionChains(driver)
main_url = "https://www.instagram.com/?utm_source=pwa_homescreen"
driver.get(main_url)
sleep(0.5)
#login part
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button').click()
sleep(0.5)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/div/label/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[4]/div/label/input').send_keys(password)
sleep(0.2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[6]/button/div').click()
sleep(6)
#save login ?
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/section/div/button').click()
sleep(5)
#notifications
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
sleep(1)
#button perfil
driver.find_element_by_xpath('/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[5]/a').click()
sleep(1)
#followers link
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/ul/li[2]/a').click()
sleep(1)
buttons = driver.find_elements_by_class_name('Pkbci')
for elem in buttons :
    try:
  # Tries to click an element
        driver.find_element_by_tag_name("button").click()
        try:
            sleep(1)
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        except:
            pass
        element = driver.find_element_by_tag_name("button")
        driver.execute_script("""
                var element = arguments[0];
                element.parentNode.removeChild(element);
                """, element)

    except ElementClickInterceptedException:
        element = driver.find_element_by_tag_name("button")
        driver.execute_script("""
                var element = arguments[0];
                element.parentNode.removeChild(element);
                """, element)
        

#for i in range(30) :
  #  try:
  #      buttons = driver.find_elements_by_tag_name('button')
   #     for j in buttons:
      #      driver.find_element_by_tag_name('button').click()
      #      try:
       #         sleep(1)
        #        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        #    except:
        #        pass
 #   except:
   #     pass
        
