from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.ball_speed = 0.05

    def move(self):
        x_coord = self.xcor() + self.x_move
        y_coord = self.ycor() + self.y_move
        self.goto(x=x_coord, y=y_coord)
        time.sleep(self.ball_speed)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = 0.05
