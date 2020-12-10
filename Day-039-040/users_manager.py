import ezsheets
import os

SHEET_KEY = os.environ["SHEET_KEY"]

sheets = ezsheets.Spreadsheet(SHEET_KEY)
users_sheet = sheets[1]
rows = users_sheet.getRows()


class UserManager:
    def __init__(self):
        print("Welcome to the Flight Club! 🤫")
        print("We find the best flight deals and email them to you.")
        self.first_name = input("What is your first name?\n")
        self.last_name = input("What is your last name?\n")
        self.email = input("What is your email?\n")
        self.confirm_email = input("Type your email again.\n")
        while self.email != self.confirm_email:
            self.confirm_email = input("Emails don't match. Type your email again.\n")

    def add_user(self):
        if self.email == self.confirm_email:
            row = [self.first_name, self.last_name, self.email]
            rows.append(row)
            users_sheet.updateRows(rows)
            print("You're in the club! 🎉")
