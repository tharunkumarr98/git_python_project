from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", fg="#FFFFFF", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="#FFFFFF")
        self.text = self.canvas.create_text(150, 125, width=280, text="Some question", fill= THEME_COLOR, font="Arial 20 italic")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        correct_button_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_button_img, highlightthickness=0, command=self.pressed_correct)
        self.correct_button.grid(row=2, column=0)
        wrong_button_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=self.pressed_wrong)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You have reached the end of the quizzler")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def pressed_correct(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def pressed_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)



