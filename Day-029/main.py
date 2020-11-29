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
    pyperclip.copy()


# ------------------ SAVE PASSWORD ------------------ #


def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) > 0 and len(email) > 0 and len(password) > 0:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you've entered:\n "
                                                              f"Website: {website}\n"
                                                              f"Email: {email}\n "
                                                              f"Password: {password}\n"
                                                              f"\n"
                                                              f"Are you sure you want to save?")

        if is_ok:
            # Write data to file
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

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
        else:
            # Show user the pwd was not saved
            message_label.config(text="Password not saved.", fg=RED, anchor="w")
            message_label.after(2000, lambda: message_label.config(text=""))
    else:
        if len(website) == 0:
            website_validation.config(text="Please fill in the website name",
                                      fg=RED,
                                      font=VALIDATION_FONT)
        if len(email) == 0:
            email_validation.config(text="Please fill in the email",
                                    fg=RED,
                                    font=VALIDATION_FONT)
        if len(password) == 0:
            password_validation.config(text="Please fill in the password",
                                       fg=RED,
                                       font=VALIDATION_FONT)


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
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

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
generate_password_btn = Button(text="Generate Password", command=generate_password)
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
