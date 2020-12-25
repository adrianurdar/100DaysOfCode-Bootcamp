from flask import Flask
import random

app = Flask(__name__)

correct_number = random.randint(0, 9)
print(correct_number)
random_colors = ["#ee2e31", "#679289", "#1d7874", "#020122", "#fc9e4f", "#f4442e"]


@app.route("/")
def index():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:number>")
def number_guess(number):
    if number < correct_number:
        return f"<h1 style='color: {random.choice(random_colors)}'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > correct_number:
        return f"<h1 style='color: {random.choice(random_colors)}'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return f"<h1 style='color: {random.choice(random_colors)}'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
