import smtplib
import ezsheets
import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
RECEIVER = os.environ["RECEIVER"]
SENDER_EMAIL = os.environ["SENDER_EMAIL"]
SENDER_PWD = os.environ["SENDER_PWD"]

SHEET_KEY = os.environ["SHEET_KEY"]
sheets = ezsheets.Spreadsheet(SHEET_KEY)
sheet_data = sheets[1]
user_emails = sheet_data.getColumn(3)
user_emails.pop(0)
print(user_emails)


class NotificationManager:
    def send_sms(self, message_to_send):
        account_sid = TWILIO_ACCOUNT_SID
        auth_token = TWILIO_AUTH_TOKEN
        receiver = RECEIVER
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=message_to_send,
                from_="+14156349707",
                to=receiver,
            )

        print(message.status)

    def send_email(self, message_to_send):
        user = SENDER_EMAIL
        password = SENDER_PWD
        for user_email in user_emails:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=user, password=password)
                connection.sendmail(
                    from_addr=user,
                    to_addrs=user_email,
                    msg=f"Subject: Low price alert! \n\n"
                        f"{message_to_send}".encode("utf-8")
                )
