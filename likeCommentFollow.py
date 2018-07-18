import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login/')


username = driver.find_element_by_name("username")
username.click();
username2 = driver.find_element_by_name("username")
username2.send_keys("") ############################################################# INPUT

password = driver.find_element_by_name("password")
password.click();
password2 = driver.find_element_by_name("password")
password2.send_keys("") ############################################################# INPUT

logLink = driver.find_element_by_tag_name('button')
logLink.click()

time.sleep(2)

arr = ["avocado", "vegan", "healthyfood", "superfood", "yum","hipster","foodporn"]
comments = ["love this!!!", "you have AMAZING posts!!", "WOW :O This is really cool!!!", "this is awesome :)", "super cool!!", "very cool!"]

for a in range(10):

    for z in range(7):

        currentSearch = "https://www.instagram.com/explore/tags/" + arr[z] + "/"
        driver.get(currentSearch)
        time.sleep(2)

        mostRecent = "//article/div[2]/div/div[1]/div[1]"
        image = driver.find_elements_by_xpath(mostRecent)
        image[0].click()
        time.sleep(2)

        profileButtonClick = driver.find_elements_by_xpath("//div[@role='dialog']/div[2]/div/article/header/div[2]/div/div/a")
        profileButtonClick[0].click()
        time.sleep(2)

        firstPicture = driver.find_elements_by_xpath("//article/div/div/div/div")
        firstPicture[0].click()
        time.sleep(2)

        for x in range(5):

            like = driver.find_elements_by_xpath("//div[@role='dialog']/div[2]/div/article/div[2]/section/span/button/span")
            if like[0].text != "Unlike":
                like[0].click()
                time.sleep(2)

            if x == 0:

                if a == 0 or a == 3 or a == 6 or a == 9:
                    myComment = driver.find_elements_by_xpath("//div[@role='dialog']/div[2]/div/article/div[2]/section[3]/form/textarea")
                    myComment[0].click()
                    time.sleep(1)

                    myComment2 = driver.find_elements_by_xpath("//div[@role='dialog']/div[2]/div/article/div[2]/section[3]/form/textarea")
                    theComment = comments[random.randint(0,5)]
                    myComment2[0].send_keys(theComment)
                    myComment2[0].send_keys(Keys.ENTER)
                    time.sleep(3)

                followButton = driver.find_elements_by_xpath("//button[contains(text(),'ollow')]")
                if followButton[0].text != "Following":
                    followButtonClick = driver.find_elements_by_xpath("//div[@role='dialog']/div[2]/div/article/header/div[2]/div/div[2]/span[2]")
                    followButtonClick[0].click()
                    time.sleep(2)

                move = driver.find_elements_by_xpath("//div[@role='dialog']/div/div/div/a")
                move[0].click()
                time.sleep(2)

            else:
                move = driver.find_elements_by_xpath("//div[@role='dialog']/div/div/div/a[2]")
                move[0].click()
                time.sleep(2)
