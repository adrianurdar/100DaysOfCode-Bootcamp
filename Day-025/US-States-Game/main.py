import turtle
import pandas
import time
from state import State

# Screen setup
screen = turtle.Screen()
screen.title("The U.S. States Game")

# Import map on the screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# # Get coordinates of mouse click
# def get_mouse_click_coord(x, y):
#     print(x, y)
#     turtle.onscreenclick(get_mouse_click_coord)
#     turtle.mainloop()


# Keep track of the correct guesses
correct_guesses = []

data = pandas.read_csv("50_states.csv")

# Use a loop to allow the user to keep guessing
game_is_on = True
while game_is_on:
    # Ask user for a guess
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state name?")

    # If user types "off" end the game
    if answer_state == "off":
        game_is_on = False
        ans = State()
        ans.color("red")
        ans.goto(0, 0)
        ans.write(f"You've scored: {len(correct_guesses)} out of 50.", align="center", font=("Courier", 40, "bold"))

    # Convert the guess to Title case
    try:
        answer_state = answer_state.title()
    except AttributeError:
        pass

    # Check if the guess is among the 50 states
    if answer_state in data.values:

        # Record the correct guesses in a list to keep track of the score
        correct_guesses.append(answer_state)

        # Write correct guess on the map
        x_cor = int(data.x[data.state == answer_state])
        y_cor = int(data.y[data.state == answer_state])
        ans = State()
        ans.move(x_cor, y_cor)
        ans.write_answer(answer_state)
        time.sleep(2)
    else:
        print("Wrong input.")

    # If user guessed all 50 states, game over
    if len(correct_guesses) == 50:
        game_is_on = False


screen.exitonclick()
