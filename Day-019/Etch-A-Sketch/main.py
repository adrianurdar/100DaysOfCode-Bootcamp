# Etch-A-Sketch Project
# "W" - move forwards
# "S" - backwards
# "A" - counter-clockwise
# "D" - clockwise
# "C" - clear drawing and put turtle in the center

from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()


def move_forward():
    return turtle.forward(10)


def move_backward():
    return turtle.backward(10)


def clear_screen():
    return screen.reset()


def turn_left():
    return turtle.setheading(turtle.heading() + 10)


def turn_right():
    return turtle.setheading(turtle.heading() - 10)


def main():
    screen.listen()
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key='d', fun=turn_right)
    screen.onkey(key="c", fun=clear_screen)
    screen.exitonclick()


if __name__ == "__main__":
    main()
