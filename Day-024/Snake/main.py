# The Snake Game Project

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# Set title and screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create the snake body
snake = Snake()

# Create the food
food = Food()

# Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake
game_is_on = True

# Create the scoreboard
score = Scoreboard()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()

        # Extend snake
        snake.extend()

        # Keep track with score and scoreboard
        score.increase_score()
        score.display_board()

    # Detect collision with wall
    if snake.head.xcor() < -300 or snake.head.xcor() > 290 or snake.head.ycor() < -280 or snake.head.ycor() > 290:
        score.reset()
        snake.reset()

    # Detect collision with own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
