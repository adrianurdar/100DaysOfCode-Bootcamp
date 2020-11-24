from turtle import Screen
from paddle import Paddle
from center_field import CenterField
from ball import Ball
from scoreboard import Scoreboard

# Setup the screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Draw center line of the screen
center_line = CenterField()
center_line.draw_center()

# Create the right paddle
right_paddle = Paddle((350, 0))

# Create left paddle
left_paddle = Paddle((-350, 0))

# Listen to events
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

# Create the ball
ball = Ball()

# Create score
scoreboard = Scoreboard()

# Turn game on
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect if the ball goes out of bounds
    if ball.xcor() > 400:
        ball.refresh()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.refresh()
        scoreboard.r_point()


screen.exitonclick()
