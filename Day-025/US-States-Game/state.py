from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)

    def move(self, x_cor, y_cor):
        self.goto(x=x_cor, y=y_cor)

    def write_answer(self, text):
        self.write(text, align=ALIGNMENT, font=FONT)
