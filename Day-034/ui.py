from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.score_label.grid(column=1, row=0, pady=20)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.quote = self.canvas.create_text(150, 125, width=280, text="Quote", font=("Arial", 15, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_answer, bd=0)
        self.true_button.grid(column=0, row=2, pady=20)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_answer, bd=0)
        self.false_button.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote, text=q_text)
        else:
            self.canvas.itemconfig(self.quote, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
