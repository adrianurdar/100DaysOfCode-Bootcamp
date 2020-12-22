import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

USER_NAME = os.environ.get("USER_NAME")
LINKEDIN_PWD = os.environ.get("LINKEDIN_PWD")
print(USER_NAME, LINKEDIN_PWD)
# Using the URL open the page by using the web driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.linkedin.com/jobs/search/?f_CF=f_WRA&f_E=1%2C2&f_JT=I&f_LF=f_AL&geoId=92000001&keywords"
           "=python%20developer&location=Remote")

# Figure out how to automatically log in to LinkedIn using Selenium
time.sleep(3)
sign_in_btn = driver.find_element_by_css_selector("body > header > nav > div > a.nav__button-secondary")
sign_in_btn.click()

time.sleep(2)
username_field = driver.find_element_by_css_selector("#username")
username_field.send_keys(USER_NAME)
password_field = driver.find_element_by_css_selector("#password")
password_field.send_keys(LINKEDIN_PWD)
password_field.send_keys(Keys.ENTER)

# Use Selenium to automatically apply to the first job that only requires you to enter your phone number
# first_job = driver.find_element_by_css_selector("#ember282")
# print(first_job.text)
# first_job.click()
# time.sleep(2)
#
# apply_now_btn = driver.find_element_by_css_selector(".jobs-apply-button")
# apply_now_btn.click()
# time.sleep(2)
#
# phone_input = driver.find_element_by_css_selector(".fb-single-line-text__input")
# phone_input.send_keys("123456789")
#
# submit_btn = driver.find_element_by_css_selector(".artdeco-button--primary")
# submit_btn.click()

# TODO: Apply to all the jobs on the page
all_jobs = driver.find_elements_by_css_selector(".artdeco-entity-lockup__title")
for job in all_jobs:
    job.click()

    # Wait for the page to load
    time.sleep(2)
    try:
        apply_now_btn = driver.find_element_by_css_selector(".jobs-apply-button")
        apply_now_btn.click()

        # Fill in the phone number input
        phone_input = driver.find_element_by_css_selector(".fb-single-line-text__input")
        phone_input.send_keys("123456789")

        # Find if submit button or next button
        submit_btn = driver.find_element_by_css_selector(".artdeco-button--primary")
        print(submit_btn.text)
        if submit_btn.text == "Next":
            # Find the close btn and click it
            close_btn = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
            close_btn.click()
            time.sleep(2)

            # Confirm
            confirm_btn = driver.find_element_by_css_selector(".artdeco-modal--layer-confirmation "
                                                              ".artdeco-button--primary")
            print(confirm_btn.text)
            confirm_btn.click()
        else:
            submit_btn.click()
    except NoSuchElementException:
        pass
