from turtle import Turtle


class CenterField(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.goto(x=0, y=-300)
        self.color("white")
        self.hideturtle()
        self.draw_center()

    def draw_center(self):
        for i in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
