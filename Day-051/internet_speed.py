import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        # Click the cookies button
        consent_btn = self.driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]')
        consent_btn.click()
        time.sleep(1)

        # Start speed test
        speed_test_btn = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                           'div[3]/div[1]/a/span[4]')
        speed_test_btn.click()
        time.sleep(60)

        # Get down/up speeds
        down_speed = self.driver.find_element_by_css_selector(".result-item-container-align-center .u-align-left span")
        self.down = float(down_speed.text)
        print(self.down)
        up_speed = self.driver.find_element_by_css_selector(".result-item-container-align-left .u-align-left span")
        self.up = float(up_speed.text)
        print(self.up)

    def tweet_at_provider(self, username, password):
        self.driver.get("https://twitter.com")
        time.sleep(2)

        # Log in
        login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div[1]'
                                                      '/div/a[2]/div')
        login_btn.click()

        username_input = self.driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n."
                                                                  "r-13qz1uu.r-417010 > main > div > div > "
                                                                  "div.css-1dbjc4n.r-13qz1uu > form > div > "
                                                                  "div:nth-child(6) > label > div > "
                                                                  "div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2."
                                                                  "r-1udh08x.r-1inuy60.r-ou255f.r-vmopo1 > div > input")
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]'
                                                           '/form/div/div[2]/label/div/div[2]/div/input')
        password_input.send_keys(password)
        time.sleep(1)
        password_input.send_keys(Keys.ENTER)

        # Compose message
        message = f"Currently on {self.down}down/{self.up}up while the minimum guarantee is 200/100. " \
                  f"What's up with that #RCS-RDS?"
        print(message)

        # Add message to tweet
        tweet_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]'
                                                        '/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div'
                                                        '/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]'
                                                        '/div/div/div/div')
        tweet_input.send_keys(message)

        # Submit tweet
        submit_tweet = self.driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz"
                                                                ".r-13qz1uu.r-417010 > main > div > div > div > div "
                                                                "> div > div.css-1dbjc4n.r-yfoy6g.r-184en5c > div "
                                                                "> div.css-1dbjc4n.r-yfoy6g.r-atwnbb > "
                                                                "div:nth-child(1) > div > div > div > div.css-1dbjc4n"
                                                                ".r-1iusvr4.r-16y2uox.r-1777fci.r-glunga.r-1bylmt5."
                                                                "r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(4) > "
                                                                "div > div > div:nth-child(2) > div.css-18t94o4.css"
                                                                "-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-"
                                                                "rs99b7.r-1w2pmg.r-1n0xq6e.r-1vuscfd.r-1dhvaqw.r-1ny"
                                                                "4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr > div "
                                                                "> span > span")
        submit_tweet.click()
