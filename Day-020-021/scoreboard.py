from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier New"
FONT_SIZE = 18
FONT_STYLE = "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.game_over()
        self.display_board()
        self.increase_score()

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_STYLE))

    def display_board(self):
        self.goto(0, +280)
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_STYLE))
