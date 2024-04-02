from tkinter import *
from quiz_brain import QuizBrain  # need this to work for the below declare parameter

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # add quiz_brain data type to be QuizBrain object as parameter
        self.quiz = quiz_brain
        # self. turn this variable which can be accessed anywhere in the class
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quiz_question = self.canvas.create_text(150, 125, width=280, text="quiz questions goes here",
                                                     font=("Arial", 20, "italic"), fill="black")
        # set width to wrap into the canvas
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # for the image, not going to use anywhere else, so no need to add .self to it
        true_btn_img = PhotoImage(file="images/true.png")
        false_btn_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_btn_img, highlightthickness=0, command=self.user_select_true)
        self.false_button = Button(image=false_btn_img, highlightthickness=0, command=self.user_select_false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.configure(bg="white")
            self.score_label.configure(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            # update question
            self.canvas.itemconfig(self.quiz_question, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_question, text="You have reached the end of the questions")
            self.true_button.config(state="disabled")  # disabled buttons
            self.false_button.config(state="disabled")

    def user_select_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def user_select_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
