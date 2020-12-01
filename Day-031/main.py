from tkinter import *
import pandas
import random

# ------------ CONSTANTS ------------ #
BACKGROUND_COLOR = "#B1DDC6"
LANG_NAME_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# ------------ DATA MANIPULATION ------------ #
try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("./data/french_words.csv")
data = df.to_dict(orient="records")
print(data)

current_word = ""


# ------------ BUTTON FUNCTIONS ------------ #
def french_version(word):
    canvas.itemconfig(lang_text, text="French")
    canvas.itemconfig(word_text, text=word["French"])
    canvas.itemconfig(canvas_img, image=card_front)


def english_version(word):
    canvas.itemconfig(lang_text, text="English")
    canvas.itemconfig(word_text, text=word["English"])
    canvas.itemconfig(canvas_img, image=card_back)


def generate_random_word():
    global current_word
    current_word = random.choice(data)
    french_version(current_word)
    window.after(1000, english_version, current_word)


def button_click(btn):
    if btn == 1:
        print(f"deleting {current_word}...")
        index_data = data.index({"French": current_word["French"], "English": current_word["English"]})
        data.remove(data[index_data])
        learn_df = pandas.DataFrame(data)
        learn_df.to_csv("./data/words_to_learn.csv", index=False)
    generate_random_word()


# ------------ USER INTERFACE ------------ #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card image
canvas = Canvas(width=800, height=525, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front)
lang_text = canvas.create_text(400, 150, text="Title", font=LANG_NAME_FONT)
word_text = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=lambda: button_click(0))
wrong_btn.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=lambda: button_click(1))
right_btn.grid(row=1, column=1)

window.mainloop()
