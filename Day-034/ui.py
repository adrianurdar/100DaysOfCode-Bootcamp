from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
RED = "#EE6587"
GREEN = "#7CDAB8"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window setup
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label widget
        self.score_label = Label(text=f"Score: {self.quiz.score} / 10", bg=THEME_COLOR, fg=WHITE)
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question text goes here.",
            width=250,
            font=FONT,
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        # True btn
        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=lambda: self.user_answer("True"))
        self.true_btn.grid(row=2, column=0)

        # False btn
        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=lambda: self.user_answer("False"))
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score} / 10")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz.\n"
                                                            f"Final Score: {int(self.quiz.score / 10 * 100)}%")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def user_answer(self, answer):
        self.user_feedback(self.quiz.check_answer(answer))

    def user_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(1000, self.get_next_question)
