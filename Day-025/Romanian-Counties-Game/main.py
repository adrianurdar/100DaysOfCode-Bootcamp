import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("The Romanian Counties Game")
screen.setup(width=1280, height=902)

image_url = "romania-map.gif"
screen.addshape(image_url)
turtle.shape(image_url)

# Keep track of all the correct answers
user_guesses = []

# Read the counties.csv
df = pandas.read_csv("counties.csv")
print(df)
counties_list = df.county.to_list()

while len(user_guesses) < 41:
    # Ask user for the name of a county
    # In the title of the input box keep track of the number of right guesses (e.g. `4/50`)
    user_input = screen.textinput(title=f"{len(user_guesses)}/41 Counties Guessed", prompt="Guess another county:")

    # User answer should be case-insensitive
    user_input = user_input.title()

    # If user types `off` show on the map and in a CSV file the remaining counties.
    if user_input == "Off" or user_input == "Exit":
        # Show score on top of the screen
        s = turtle.Turtle()
        s.hideturtle()
        s.speed(0)
        s.color("black")
        s.penup()
        s.goto(0, 350)
        s.write(f"You've named {len(user_guesses)} counties out of 41", align="center",
                font=("Courier", 15, "bold"))

        # Put all the remaining counties on the map
        for county in counties_list:
            if county not in user_guesses:
                # Take coord of the county
                x_cor = float(df.x[df.county == county])
                y_cor = float(df.y[df.county == county])

                # Create a turtle to write the result
                r = turtle.Turtle()
                r.hideturtle()
                r.speed(0)
                r.color("yellow")
                r.penup()
                r.goto(x_cor, y_cor)
                r.write(county, align="left", font=("Courier", 13, "bold"))

        # End game
        break

    # If the user guessed correctly, the name of the county should be placed on the map at the corresponding
    # coordinates.
    if user_input in counties_list:
        # Append correct guess to the list
        user_guesses.append(user_input)

        # Get coord of that county
        x_cor = float(df.x[df.county == user_input])
        y_cor = float(df.y[df.county == user_input])

        # Create a turtle to write the county in the position
        t = turtle.Turtle()
        t.color("white")
        t.hideturtle()
        t.penup()
        t.goto(x_cor, y_cor)
        t.write(user_input, align="left", font=("Courier", 13, "bold"))
        time.sleep(3)

    # If the user guessed wrong, nothing happens and the input box should prompt him for another answer.
    else:
        pass


screen.exitonclick()
