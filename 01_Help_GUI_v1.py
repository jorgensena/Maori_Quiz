"""
Create the Main Welcome GUI

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

        # Maori Quiz Heading (row 0)
        self.maori_quiz_label = Label(text="Maori Quiz",
                                          font=("Comic Sans MS", "20", "bold",
                                                "underline"),
                                          bg=bg_colour, fg=font_colour,
                                          padx=10, pady=10)
        self.maori_quiz_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Quiz")
    something = Welcome()
    root.mainloop()
