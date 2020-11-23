# Turtle Race Project

from turtle import Turtle, Screen
import random

screen = Screen()

colors = {
    "red": {
        "y-axis": -150
    },
    "orange": {
        "y-axis": -100
    },
    "yellow": {
        "y-axis": -50
    },
    "violet": {
        "y-axis": 0
    },
    "blue": {
        "y-axis": 50
    },
    "indigo": {
        "y-axis": 100
    },
    "green": {
        "y-axis": 150
    }
}


def create_turtle(color, y):
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=0+y)
    return turtle


def main():
    # Screen setup
    screen.setup(width=500, height=400)

    is_race_on = False

    # Ask user to bet on the winning color
    player_bet = screen.textinput("Make Your Bet", "Who will win the race? Enter a colour: ")

    # Create 7 turtles (Red, Orange, Yellow, Violet, Blue, Indigo, Green) and send them to starting line
    all_turtles = []

    for key in colors:
        new_turtle = create_turtle(color=key, y=colors[key]["y-axis"])
        all_turtles.append(new_turtle)

    if player_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == player_bet:
                    print(f"You win! The {winning_color} turtle is the winner.")
                else:
                    print(f"You lose. The {winning_color} turtle is the winner.")

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

    screen.exitonclick()


if __name__ == "__main__":
    main()
