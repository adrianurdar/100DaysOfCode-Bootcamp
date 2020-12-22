import os
from internet_speed import InternetSpeedTwitterBot

PROMISED_DOWN = 200
PROMISED_UP = 100

TWITTER_EMAIL = os.environ.get("TW_EMAIL")
TWITTER_PWD = os.environ.get("TW_PWD")

browser = InternetSpeedTwitterBot()
browser.get_internet_speed()

browser.tweet_at_provider(username=TWITTER_EMAIL, password=TWITTER_PWD)
