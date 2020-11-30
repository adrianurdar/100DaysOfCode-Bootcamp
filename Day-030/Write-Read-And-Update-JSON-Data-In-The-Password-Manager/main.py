import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ------------------ CONSTANTS ------------------ #
GREEN = "#7CDAB8"
RED = "#EE6587"
FONT = ("Helvetica", 13, "normal")
VALIDATION_FONT = ("Helvetica", 11, "normal")


# ------------------ PASSWORD GENERATOR ------------------ #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += ([choice(symbols) for _ in range(randint(2, 4))])
    password_list += ([choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ------------------ FIND PASSWORD ------------------ #
def find_password():
    website = website_input.get()

    if len(website) == 0:
        website_validation.config(text="Please fill in the website name",
                                  fg=RED,
                                  font=FONT)
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title="File Not Found.", message="No Data File Found")
        else:
            try:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=f"Found {website_input.get()}", message=f"Email: {email}\n"
                                                                                  f"Password: {password}")

                email_input.delete(0, END)
                email_input.insert(0, email)
                password_input.insert(0, password)
                pyperclip.copy(password)
                message_label.config(text="Password copied to clipboard!", fg=GREEN, anchor="w")
                message_label.after(2000, lambda: message_label.config(text=""))
            except KeyError:
                messagebox.showwarning(title="Key Not Found", message="No Details For The Website Exists")
                website_input.delete(0, END)
                website_input.focus()


# ------------------ SAVE PASSWORD ------------------ #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0:
        website_validation.config(text="Please fill in the website name",
                                  fg=RED,
                                  font=VALIDATION_FONT)
    elif len(email) == 0:
        email_validation.config(text="Please fill in the email",
                                fg=RED,
                                font=VALIDATION_FONT)
    elif len(password) == 0:
        password_validation.config(text="Please fill in the password",
                                   fg=RED,
                                   font=VALIDATION_FONT)
    else:
        try:
            with open("data.json", "r") as file:
                # Read old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Write data to file
                json.dump(data, file, indent=4)
        finally:
            # Clear the fields
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_validation.config(text="", font=("Helvetica", 1, "normal"))
            email_validation.config(text="", font=("Helvetica", 1, "normal"))
            password_validation.config(text="", font=("Helvetica", 1, "normal"))

            # Send cursor to website label
            website_input.focus()

            # Show user a confirmation message
            message_label.config(text="Password saved successfully!", fg=GREEN, anchor="w")
            message_label.after(2000, lambda: message_label.config(text=""))


# ------------------ UI ------------------ #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo widget
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website label widget
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

# Website input widget
website_input = Entry(width=21)
website_input.focus()
website_input.grid(row=1, column=1)

# Website search button widget
website_search_button = Button(width=14, text="Search", command=find_password)
website_search_button.grid(row=1, column=2)

# Website validation label widget
website_validation = Label(width=35, font=("Helvetica", 1, "normal"))
website_validation.grid(row=2, column=1, columnspan=2)

# Email label widget
email_label = Label(text="Email/Username")
email_label.grid(row=3, column=0)

# Email input widget
email_input = Entry(width=35)
email_input.grid(row=3, column=1, columnspan=2)
email_input.insert(0, "adrian.urdar@gmail.com")

# Email validation label widget
email_validation = Label(width=35, font=("Helvetica", 1, "normal"))
email_validation.grid(row=4, column=1, columnspan=2)

# Password label widget
password_label = Label(text="Password")
password_label.grid(row=5, column=0)

# Password input widget
password_input = Entry(width=21)
password_input.grid(row=5, column=1)

# Generate password button widget
generate_password_btn = Button(width=14, text="Generate Password", command=generate_password)
generate_password_btn.grid(row=5, column=2)

# Password validation
password_validation = Label(width=35, font=("Helvetica", 1, "normal"))
password_validation.grid(row=6, column=1, columnspan=2)

# Add button widget
add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(row=8, column=1, columnspan=2)

# Error or confirmation message
message_label = Label(width=21)
message_label.grid(row=9, column=1)


window.mainloop()
