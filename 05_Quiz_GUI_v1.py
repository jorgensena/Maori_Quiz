"""
Create a Quiz GUI
Gets copy of Welcome GUI from 01_Help_GUI_v1
Open the Quiz GUI by a button from the main screen

By Amy Jorgensen
17/05/22
"""
from tkinter import *


class Welcome:
    def __init__(self):
        print("hello world")

        # formatting variables
        bg_colour = "#FFF4D9"  # pale yellow
        font_colour = "#990000"  # dark red

        # Quiz Main Screen GUI
        self.main_frame = Frame(width=300, height=300, bg=bg_colour)
        self.main_frame.grid()

        # Maori Quiz Heading (row 0)
        self.maori_main_label = Label(self.main_frame, text="Maori Quiz",
                                      font=("Comic Sans MS", "20", "bold",
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
        self.button_frame = Frame(self.main_frame, bg=bg_colour)
        self.button_frame.grid(row=2)

        # Help Button (row 0)
        self.help_button = Button(self.button_frame, text="Help",
                                  font=("Comic Sans MC", "14"),
                                  padx=10, pady=10, bg=bg_colour,
                                  fg=font_colour, command=self.help)
        self.help_button.grid(column=0, pady=10)


    def help(self):
        print("You asked for help")

    def quiz(self):
        print("You want to start the quiz")
        Quiz()


class Quiz:
    def __init__(self):
        print("You wanted to do the quiz :)")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Quiz")
    something = Welcome()
    root.mainloop()


