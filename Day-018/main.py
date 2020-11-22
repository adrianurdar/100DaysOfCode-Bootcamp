# The Hirst Paining Project
# Create a painting with 10 by 10 rows of spots
# Each dot should be 20 in size and 50 spacing between them

from turtle import Turtle, Screen
import random


def main():
    # Color palette
    color_list = [
        (203, 164, 109),
        (154, 75, 48),
        (223, 201, 135),
        (53, 94, 125),
        (173, 153, 39),
        (137, 31, 20),
        (133, 163, 185),
        (199, 92, 72),
        (46, 123, 87),
        (72, 44, 36),
        (13, 98, 72),
        (145, 179, 147),
        (93, 73, 75),
        (233, 176, 165),
        (161, 143, 159),
        (54, 46, 51),
        (184, 205, 172),
        (35, 61, 75),
        (21, 85, 90),
        (153, 17, 19),
        (84, 147, 130),
        (39, 66, 90),
        (184, 89, 93),
        (11, 73, 67),
        (105, 127, 155),
        (218, 177, 182)
    ]

    # Define turtle and screen
    turtle = Turtle()
    screen = Screen()

    # Turtle speed
    turtle.speed(0)

    # Hide turtle
    turtle.hideturtle()

    # Setup screen mode to 255
    screen.colormode(255)

    # Make the turtle start from left bottom corner
    turtle.penup()
    turtle.sety(-300)

    for j in range(10):
        turtle.penup()
        turtle.sety(turtle.ycor() + 50)
        turtle.setx(-250)
        for i in range(10):
            turtle.color(random.choice(color_list))
            turtle.dot(20)
            turtle.penup()
            turtle.forward(50)
            turtle.pendown()

    screen.exitonclick()


if __name__ == "__main__":
    main()
