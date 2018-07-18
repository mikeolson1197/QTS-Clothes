import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login/')


driver.implicitly_wait(5) # seconds
username = driver.find_element_by_name("username")
username.click();
username2 = driver.find_element_by_name("username")
username2.send_keys("") ############################################################# INPUT
driver.implicitly_wait(5) # seconds


password = driver.find_element_by_name("password")
password.click();
password2 = driver.find_element_by_name("password")
password2.send_keys("") ############################################################# INPUT

logLink = driver.find_element_by_tag_name('button')
logLink.click()

driver.implicitly_wait(5)
time.sleep(2)

driver.refresh()
time.sleep(2)


for y in range(50):

    driver.get('https://www.instagram.com/getyoselfclothes/')
    time.sleep(2)

    following = driver.find_elements_by_xpath("//header/section/ul/li[3]/a")
    following[0].click()
    time.sleep(2)

    string = "//div[@role='dialog']/div[2]/div/div[2]/ul/div/li/div/div/a"
    person = driver.find_elements_by_xpath(string)
    person[0].click()
    time.sleep(2)

    unfollowString = "//button[contains(text(),'Following')]"
    #unfollowString = "//header/section/div[2]/span/"
    unfollow = driver.find_elements_by_xpath(unfollowString)
    unfollow[0].click()
    time.sleep(2)
