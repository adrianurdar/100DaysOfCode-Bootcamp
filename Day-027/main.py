# Mile to Km Converter
from tkinter import *

FONT = ("Arial", 18, "normal")


def calculate():
    miles = float(user_input.get())
    miles_to_km = round(miles * 1.609, 2)
    result["text"] = miles_to_km


# Screen setup
screen = Tk()
screen.title("Miles To Kilometer Converter")
screen.minsize(width=350, height=150)
screen.config(padx=50, pady=50)

# User input widget
user_input = Entry(width=7)
user_input.grid(row=0, column=1)

# "Miles" label widget
miles_label = Label()
miles_label.config(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

# "is equal to" label widget
is_equal_to = Label()
is_equal_to.config(text="is equal to", font=FONT)
is_equal_to.grid(row=1, column=0)

# Result label widget
result = Label()
result.config(text="0", font=FONT)
result.grid(row=1, column=1)

# "Km" label widget
km = Label()
km.config(text="Km", font=FONT)
km.grid(row=1, column=2)

# "Calculate" button widget
calculate_btn = Button(text="Calculate", command=calculate)
calculate_btn.grid(row=2, column=1)

# Keep screen open
screen.mainloop()
