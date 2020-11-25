from turtle import Turtle
import random
import time

COLORS = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple"
]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.x_start_cor = random.randint(-200, 350)
        self.x_refresh_cor = random.randint(300, 350)
        self.y_cor = random.randint(-260, 280)
        self.goto(x=self.x_start_cor, y=self.y_cor)
        self.x_move = MOVE_INCREMENT
        self.car_speed = 0.01

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
        time.sleep(self.car_speed)

    def increase_speed(self):
        self.goto(x=self.x_start_cor, y=self.y_cor)
        self.move()
        self.car_speed *= 0.9

    def refresh(self):
        if self.xcor() < -320:
            self.goto(x=self.x_refresh_cor, y=self.y_cor)
