"""
Create a Help GUI

By Amy Jorgensen
05/05/22
"""
from tkinter import *


class Welcome:
    def __init__(self):
        print("hello world")

        # formatting variables
        bg_colour = "#FFF4D9"  # pale yellow
        font_colour = "#990000"  # dark red

        # Quiz Main Screen GUI
        self.quiz_frame = Frame(width=300, height=300, bg=bg_colour)
        self.quiz_frame.grid()

        # Frame for button border with black border color
        button_border = Frame(highlightbackground = font_colour,
                              highlightthickness = 1, bd=0)

        # Maori Quiz Heading (row 0)
        self.maori_quiz_label = Label(self.quiz_frame, text="Maori Quiz",
                                      font=("Comic Sans MS", "20", "bold",
                                            "underline"),
                                      bg=bg_colour, fg=font_colour,
                                      padx=10, pady=10)
        self.maori_quiz_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.quiz_frame, text="Help",
                                  font=("Comic Sans MC", "14"),
                                  padx=10, pady=10, bg="#f5c4e0",
                                  command=self.help).grid(row=1)

    def help(self):
        print("You asked for help")
        Help()


class Help():
    pass

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Quiz")
    something = Welcome()
    root.mainloop()
