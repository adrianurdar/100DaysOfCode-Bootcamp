# Birthday Wisher (Extra-hard)
import datetime as dt
import smtplib
import pandas
import random

# 1. Update the birthdays.csv
# Name,Email,YYYY,MM,DD

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()

birthday_df = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_df.set_index("name").T.to_dict()

for key in birthday_dict:
    if now.month == birthday_dict[key]["month"] and now.day == birthday_dict[key]["day"]:
        birthday_name = key
        birthday_email = birthday_dict[key]["email"]

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        letter_template = f"letter_{random.randint(1, 3)}.txt"
        with open(f"./letter_templates/{letter_template}") as file:
            letter_content = file.read()
        letter_content = letter_content.replace("[NAME]", birthday_name)
        print(letter_content)

        # 4. Send the letter generated in step 3 to that person's email address.
        user = "****@gmail.com"
        password = "****"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=user, password=password)
            connection.sendmail(
                from_addr=user,
                to_addrs=birthday_email,
                msg=f"Subject: Happy bday! \n\n"
                    f"{letter_content}".encode("utf-8")
            )
