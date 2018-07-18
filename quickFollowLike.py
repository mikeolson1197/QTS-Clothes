
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

arr = ["avocado", "vegan", "healthyfood", "superfood"]
for z in range(5):
    currentSearch = "https://www.instagram.com/explore/tags/" + arr[z] + "/"
    driver.get(currentSearch)
    for x in range(4):
        for y in range(3):

            row = x + 1
            col = y + 1
            string = "//article/div[2]/div/div[" + str(row) + "]/div[" + str(col) + "]/a"
            elem = driver.find_elements_by_xpath(string)
            driver.get(elem[0].get_attribute("href"))

            followButton = driver.find_elements_by_xpath("//button")
            if followButton[0].text != "Following":
                followButton[0].click()

            like = driver.find_elements_by_xpath("//article/div[2]/section/span/button/span")
            if like[0].text != "Unlike":
                like[0].click()

            driver.get(currentSearch)
