import smtplib

SENDER_EMAIL = "pythonappacc"
SENDER_PWD = "6CvkqG1lloWxPie&hT#&"


def send_email(message_to_send):
    user = SENDER_EMAIL
    password = SENDER_PWD
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(
            from_addr=user,
            to_addrs="adrian.urdar@gmail.com",
            msg=f"Subject: Low price alert! \n\n"
                f"{message_to_send}".encode("utf-8")
        )
