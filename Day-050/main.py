import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

FB_USERNAME = os.environ.get("FB_USERNAME")
FB_PWD = os.environ.get("FB_PWD")


# Using Selenium and Python Navigate to the Tinder website (https://tinder.com/)
#  and click on LOG IN then LOGIN WITH FACEBOOK
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://tinder.com")

time.sleep(2)
login_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div'
                                         '/header/div/div[2]/div[2]/button')
login_btn.click()

time.sleep(2)
login_with_fb_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/'
                                                 'span/div[2]/button')
login_with_fb_btn.click()


# Login with FB
all_windows = driver.window_handles
tinder_window = all_windows[0]
fb_login_window = all_windows[1]

# Switch to FB login window
driver.switch_to.window(fb_login_window)
print(driver.title)

# Fill in the Facebook login form and submit it to log in
fb_username = driver.find_element_by_xpath('//*[@id="email"]')
fb_username.send_keys(FB_USERNAME)

fb_pwd = driver.find_element_by_xpath('//*[@id="pass"]')
fb_pwd.send_keys(FB_PWD)
fb_pwd.send_keys(Keys.ENTER)

# Switch back to tinder window
driver.switch_to.window(tinder_window)
print(driver.title)


# Using Selenium and Python: Click ALLOW for location, click NOT INTERESTED for notifications,
#  click I ACCEPT for cookies

time.sleep(5)

allow_location_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_btn.click()

notifications_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_btn.click()

cookies_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies_btn.click()

# Hit Like (free tier is 100 likes per day)
for _ in range(100):
    # Click on the "Like" button (add at least 1 sec)
    try:
        time.sleep(1)
        like_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div'
                                                '/div[2]/div[4]/button')
        like_btn.click()

    # If the like btn didn't load
    except NoSuchElementException:
        time.sleep(2)
        _ -= 1

    # Dismiss matches by clicking on "BACK TO TINDER" to continue swiping
    except ElementClickInterceptedException:
        back_to_tinder_btn = driver.find_element_by_css_selector(".itsAMatch a")
        back_to_tinder_btn.click()
        time.sleep(1)

driver.close()
