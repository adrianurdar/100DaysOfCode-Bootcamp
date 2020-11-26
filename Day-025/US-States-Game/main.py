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
states_left = []

data = pandas.read_csv("50_states.csv")

# Use a loop to allow the user to keep guessing
game_is_on = True
while game_is_on:
    # Ask user for a guess
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state name?")

    # Convert the guess to Title case
    try:
        answer_state = answer_state.title()
    except AttributeError:
        pass

    # If user types "off" end the game, show him all the states he didn't guess and also place them in a CSV
    if answer_state == "Off":
        game_is_on = False

        # Put all states he didn't guess in a CSV
        for state in data.values:
            if state[0] not in correct_guesses:
                states_left.append(state[0])

        # Write the remaining states with red on map
        for state in states_left:
            ans = State()
            ans.hideturtle()
            ans.color("red")
            x_cor = int(data.x[data.state == state])
            y_cor = int(data.y[data.state == state])
            ans.goto(x_cor, y_cor)
            ans.write_answer(state)

        data_dict = {
            "States Left": states_left
        }

        df = pandas.DataFrame(data_dict)
        df.to_csv("result.csv")

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
