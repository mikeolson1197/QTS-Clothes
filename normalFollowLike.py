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

driver.implicitly_wait(10)

arr = ["avocado", "vegan", "healthyfood", "superfood", "shirt","hipster","clothes"]
for z in range(7):

    currentSearch = "https://www.instagram.com/explore/tags/" + arr[z] + "/"
    driver.get(currentSearch)
    driver.refresh()
    mostRecent = "//article/div[2]/div/div[1]/div[1]"
    image = driver.find_elements_by_xpath(mostRecent)

    image[0].click()

    for x in range(12):

        time.sleep(7)
        like = driver.find_elements_by_xpath("//div[@role='dialog']/div[2]/div/article/div[2]/section/span/button/span")
        if like[0].text != "Unlike":
            like[0].click()

        time.sleep(7)
        followButton = driver.find_elements_by_xpath("//button[contains(text(),'ollow')]")
        if followButton[0].text != "Following":
            followButtonClick = driver.find_elements_by_xpath("//div[@role='dialog']/div[2]/div/article/header/div[2]/div/div[2]/span[2]")
            followButtonClick[0].click()

        time.sleep(7)
        move = driver.find_elements_by_xpath("//div[@role='dialog']/div/div/div/a[2]")
        move[0].click()
