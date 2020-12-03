import requests
from datetime import datetime
import sched
import time
import smtplib

# My latitude
MY_LAT = 45.649490
min_lat = 40
max_lat = 50
# My longitude
MY_LONG = 25.606550
min_long = 20
max_long = 30

schedule = sched.scheduler(time.time, time.sleep)

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_within_range():
    if min_lat < 45.45 < max_lat and min_long < 25 < max_long:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


def is_dark():
    if sunrise < time_now.hour < sunset:
        return False
    else:
        return True


# If the ISS is close to my current position and it is currently dark
# Then send me an email to tell me to look up.
def send_email():
    if is_within_range() and is_dark():
        user = "****@gmail.com"
        password = "****"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=user, password=password)
            connection.sendmail(
                from_addr=user,
                to_addrs="a****r@gmail.com",
                msg="Subject: ISS is above \n\n"
                    "Look Up ☝️"
            )
    schedule.enter(60, 1, send_email)


# BONUS: run the code every 60 seconds.
schedule.enter(60, 1, send_email)
schedule.run()
