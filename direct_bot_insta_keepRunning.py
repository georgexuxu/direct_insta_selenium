
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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
#open direct-page
driver.find_element_by_xpath('/html/body/div[1]/section/nav[1]/div/div/header/div/div[2]/a/div/div/div').click()
sleep(1)
#trash trash trash
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
sleep(1)
driver.find_element_by_xpath('/html/body').click()
sleep(1)
#open blue dot
# DOT: 

#driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/div/div/div[2]/div/div[1]/a/div/div[3]/div') == False
def respond():
    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/div/div/div[2]/div/div[1]/a/div/div[3]/div').click()
            sleep(0.5)
            #save msg for search
            msg = driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/span').get_attribute("innerHTML")
            sleep(0.5)
            #getting result
            driver.execute_script("window.open('https://www.google.com/','_blank');")
            sleep(0.5)
            driver.switch_to_window(driver.window_handles[1])
            #sleep(0.1)
            driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/form').click()
            sleep(0.5)
            driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[1]/input').send_keys('wikipedia '+ msg)
            driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[1]/input').send_keys(Keys.RETURN)
            sleep(0.5)

            driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/div/a/div[2]/div').click()

            wiki_link = driver.current_url
            driver.close()
            driver.switch_to_window(driver.window_handles[0])
            sleep(0.2)
            #sendign result
            driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div/textarea').send_keys(wiki_link)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div/div/div[2]/div/div/div[2]/button').click()
            #clean direct

            driver.find_element_by_xpath('/html/body/div[1]/section/div[1]/header/div/div[2]/button').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div/div[3]/div[1]/button/div').click()
            sleep(7)
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/button[1]').click()
            sleep(1)
            respond()
        
        except :
            sleep(3)
            respond()
respond()
