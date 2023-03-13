from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"




class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)
        self.label1 = Label(text="Score: 0", bg=THEME_COLOR,fg="white")
        self.canvas = Canvas(width=300,height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280,text="Sample Text", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.label1.grid(column=1, row=0)
        self.score = 0
        true = PhotoImage(file="images/true.png")

        self.true_button = Button(image=true, highlightthickness=0, command=self.right)
        self.true_button.grid(row=2, column=0)

        false = PhotoImage(file="images/false.png")

        self.false_button = Button(image=false, highlightthickness=0, command=self.left)
        self.false_button.grid(row=2, column=1)


        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= f"You've finished the quiz!!!\nWith final score of {self.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def right(self):
        user_answer = "True"
        is_right = self.quiz.check_answer(user_answer)
        if is_right:
            self.score += 1
            self.label1.config(text=f"Score: {self.score}")
            self.good()
        else:
            self.bad()


    def left(self):
        user_answer = "False"
        is_right = self.quiz.check_answer(user_answer)
        if is_right:
            self.score +=1
            self.label1.config(text=f"Score: {self.score}")
            self.good()
        else:
            self.bad()


    def good(self):
        self.canvas.config(bg="green")
        self.window.after(1000, self.get_next_question)


    def bad(self):
        self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
