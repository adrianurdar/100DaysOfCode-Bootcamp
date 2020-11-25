from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# Create the player
player = Player()
screen.listen()
screen.onkey(player.up, "Up")

# Create the scoreboard
score = Scoreboard()

# Create cars
counter = 0
cars = []
while counter < 20:
    new_car = CarManager()
    new_car.goto(random.randint(-200, 350), random.randint(-300, 300))
    cars.append(new_car)
    counter += 1

game_is_on = True
while game_is_on:
    screen.update()

    for car in cars:
        # Car move
        car.move()

        # Once the car reaches the left side of the screen, reset it's position
        car.refresh()

        # Detect collision and finish game
        if car.distance(player) < 15:
            score.game_over()
            game_is_on = False

    # If player reaches the end, level-up
    if player.ycor() >= 280:
        score.level_up()
        player.refresh()
        for car in cars:
            car.increase_speed()

screen.exitonclick()
