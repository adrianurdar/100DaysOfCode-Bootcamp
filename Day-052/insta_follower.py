import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

IG_EMAIL = os.environ.get("IG_EMAIL")
IG_PWD = os.environ.get("IG_PWD")

SIMILAR_ACCOUNT = "chefilacutite"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        # Accept cookies
        cookies = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC "
                                                           "> button.aOOlW.bIiDR")
        cookies.click()
        time.sleep(1)

        # login
        username_input = self.driver.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label "
                                                                  "> input")
        username_input.send_keys(IG_EMAIL)
        pwd_input = self.driver.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label "
                                                             "> input")
        pwd_input.send_keys(IG_PWD)
        pwd_input.send_keys(Keys.ENTER)
        time.sleep(2)

    def find_followers(self):
        search_similar_account = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div'
                                                                   '/div[2]/input')
        search_similar_account.send_keys(SIMILAR_ACCOUNT)
        time.sleep(2)
        search_element = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/'
                                                           'div[4]/div/a[1]')
        search_element.click()
        time.sleep(2)

        # Click on followers
        followers = self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section "
                                                             "> ul > li:nth-child(2) > a")
        followers.click()
        time.sleep(2)

        element_inside_pop_up = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element_inside_pop_up)
            time.sleep(2)

    def follow(self):
        elements = self.driver.find_elements_by_css_selector("li button")
        for element in elements:
            try:
                element.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
