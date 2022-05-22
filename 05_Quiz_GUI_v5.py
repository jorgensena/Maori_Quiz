"""
Add the other set of questions (maori to int)

By Amy Jorgensen
22/05/22
"""
from tkinter import *
from functools import partial
import random


class Welcome:
    def __init__(self):

        # formatting variables
        bg_colour = "#FFF4D9"  # pale yellow
        font_colour = "#990000"  # dark red
        btn_colour = "#FFFFCC"  # pale yellow

        # Welcome Main Screen GUI
        self.main_frame = Frame(width=300, height=300, bg=bg_colour)
        self.main_frame.grid()

        # Maori Welcome Heading (row 0)
        self.maori_main_label = Label(self.main_frame, text="Maori Quiz",
                                      font=("Comic Sans MS", "30", "bold",
                                            "underline"),
                                      bg=bg_colour, fg=font_colour,
                                      padx=10, pady=10)
        self.maori_main_label.grid(row=0)

        # Quiz button (row 1)
        self.quiz_button = Button(self.main_frame, text="Start Quiz",
                                  font=("Comic Sans MC", "14"),
                                  padx=10, pady=10, bg="#D5E8D4",
                                  fg=font_colour, command=self.quiz)
        self.quiz_button.grid(row=1)

        # Button frame (row 2) (for help and dismiss btns)
        self.main_button_frame = Frame(self.main_frame, bg=bg_colour)
        self.main_button_frame.grid(row=2)

        # Help Button (row 0)
        self.help_button = Button(self.main_button_frame, text="Help",
                                  font=("Comic Sans MC", "14"),
                                  padx=10, pady=10, bg=btn_colour,
                                  fg=font_colour, command=self.help)
        self.help_button.grid(column=0, pady=10)


    def help(self):
        print("You asked for help")

    def quiz(self):
        Quiz(self)


class Quiz:
    def __init__(self, partner):
        print("You want to do the quiz :)")

        # formatting variables
        bg_colour = "#FFF4D9"  # pale yellow
        font_colour = "#990000"  # dark red
        btn_colour = "#FFFFCC"  # pale yellow

        self.counter = 0
        # Maori numbers
        self.maori_q = [["Tahi", 1], ["Rua", 2], ["Toru", 3], ["Wha", 4],
                        ["Rima", 5], ["Ono", 6], ["Whitu", 7], ["Waru", 8],
                        ["Iwa", 9], ["Tekau", 10]]
        # potential question position
        self.q_num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        partner.quiz_button.config(state=DISABLED)

        # Open new window
        self.quiz_box = Toplevel()

        # If user uses cross to exit, quiz button is enabled
        self.quiz_box.protocol("WM_DELETE_WINDOW", partial(self.close_quiz,
                                                           partner))

        # Quiz Frame GUI
        self.quiz_frame = Frame(self.quiz_box, bg=bg_colour)
        self.quiz_frame.grid()

        # Quiz Heading (row 0)
        self.quiz_heading = Label(self.quiz_frame, text="Maori Quiz",
                                  font=("Comic Sans MS", "30", "bold",
                                        "underline"),
                                  bg=bg_colour, fg=font_colour,
                                  padx=10, pady=10)
        self.quiz_heading.grid(row=0)

        # Questions Label (row 1)
        self.question_label = Label(self.quiz_frame,
                                    text="Questions go here...",
                                    font=("Comic Sans MS", "16"),
                                    bg=bg_colour, fg=font_colour,
                                    padx=10, pady=10)
        self.question_label.grid(row=1)

        # Small message label (row 2)
        self.message_label = Label(self.quiz_frame,
                                   text="Write your answer below",
                                   font=("Comic Sans MS", "10"),
                                   bg=bg_colour, fg=font_colour)
        self.message_label.grid(row=2)

        # Question entry box (row 3)
        self.question_entry = Entry(self.quiz_frame, width=20, justify=CENTER,
                                    font=("Comic Sans MS", "14"))
        self.question_entry.grid(row=3, padx=10)

        # Button frame for 'Next' and 'Check' btns (row 4)
        self.quiz_button_frame = Frame(self.quiz_frame, bg=bg_colour)
        self.quiz_button_frame.grid(row=4)

        # 'Check' button (column 0)
        self.check_button = Button(self.quiz_button_frame, text="Check",
                                   font=("Comic Sans MS", "14"),
                                   bg="#D5E8D4",  # pale green
                                   fg=font_colour,
                                   command=self.check_question)
        self.check_button.grid(row=0, column=0, padx=5, pady=10)

        # 'Next' button (column 0)
        # When window opens says Start to start the quiz
        self.next_button = Button(self.quiz_button_frame, text="Start",
                                  font=("Comic Sans MS", "14"),
                                  bg="#D4E1F5",  # pale blue
                                  fg=font_colour,
                                  command=self.change_question)
        self.next_button.grid(row=0, column=1, padx=5, pady=10)

        # Dismiss button (row 5)
        self.dismiss_button = Button(self.quiz_frame, text="Dismiss",
                                     font=("Comic Sans MS", "14"),
                                     bg=btn_colour, fg=font_colour,
                                     command=partial(self.close_quiz, partner))
        self.dismiss_button.grid(row=5, pady=10)

    # Method to check question
    def check_question(self):
        error = "#ebc091"  # Pale orange bg for when entry box has an error
        font_colour = "#990000"  # dark red
        has_errors = False
        # Retrieve answer entered into Entry field
        to_check = self.question_entry.get()
        if self.counter <= 5:
            try:
                to_check = int(to_check)
                self.question_entry.config(bg="white")
                # Check answer and print output
                if to_check == self.question[1]:
                    self.message_label.config(fg=font_colour,
                                              text="Yay! You got it correct!")
                else:
                    self.message_label.config(fg=font_colour,
                                              text="Oops! That was incorrect")

            except ValueError:
                self.message_label.config(text="Enter an integer number!",
                                          fg="black")
                self.question_entry.config(bg=error)
                has_errors = True
        else:
            to_check = to_check.title()
            # Check answer and print output
            if to_check == self.question[0]:
                self.question_entry.config(bg="white")
                self.message_label.config(fg=font_colour,
                                          text="Yay! You got it correct")
            elif not to_check:
                self.message_label.config(text="You left it blank!",
                                          fg="black")
                self.question_entry.config(bg=error)
                has_errors = True
            else:
                self.question_entry.config(bg="white")
                self.message_label.config(fg=font_colour,
                                          text="Oops! That was incorrect")
        if not has_errors and self.counter != 10:
            self.next_button.config(state=NORMAL)

        if self.counter == 10:
            self.message_label.config(text="")
            self.question_label.config(text="End of Quiz")


    # Method to change the quiz_label to show the next question
    def change_question(self):
        self.next_button.config(text="Next")
        self.message_label.config(text="Write your answer below")
        # the quiz is 10 questions
        if self.counter != 10:
            self.question, self.q_num_list = next_q(self.maori_q, self.q_num_list)
            # First 5 questions convert to integer
            if self.counter < 5:
                self.question_label.config(text=f"What is {self.question[0]}?")
            # Last 5 questions convert to Maori
            else:
                self.question_label.config(text=f"What is {self.question[1]}?")

            self.counter += 1
            # Disable the 'next' button after changing the question
            self.next_button.config(state=DISABLED)


    # Method to close the quiz GUI
    def close_quiz(self, partner):
        # Put help button back to normal
        partner.quiz_button.config(state=NORMAL)
        self.quiz_box.destroy()


# Function to get the next question
def next_q(q_list, q_num):
    num = random.choice(q_num)
    q_num.remove(num)
    # return random question and new number list
    return q_list[num], q_num


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Quiz")
    something = Welcome()
    root.mainloop()


