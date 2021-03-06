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
                                  padx=10, pady=10, bg="white",
                                  command=self.help)
        self.help_button.grid(row=1, pady=10)

    def help(self):
        print("You asked for help")
        Help()


class Help:
    def __init__(self):
        # formatting variables
        bg_colour = "#FFF4D9"  # pale yellow
        font_colour = "#990000"  # dark red

        # set up child window
        self.help_box = Toplevel()

        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=bg_colour)
        self.help_frame.grid()

        # set up help heading (row 0)
        self.help_heading = Label(self.help_frame, text="Help/Instructions",
                                  font=("Comic Sans MS", "20", "bold",
                                        "underline"),
                                  bg=bg_colour, fg=font_colour)
        self.help_heading.grid(row=0)

        # Help text (row 1)
        self.help_text = Label(self.help_frame,
                               text="\nThis is a quick 10 question quiz on Maori "
                                    "numbers (1-10). You could be asked to "
                                    "translate from Maori to integer, or "
                                    "integer to Maori."
                                    "\n"
                                    "\nEnter your answer to the "
                                    "question into the box and push 'check' to"
                                    " see it is correct. Then push next to go "
                                    "to the next question. "
                                    "\n"
                                    "\nTo see your most "
                                    "recent results, push 'RESULTS' to see "
                                    "your most recent mistake and 3 most "
                                    "recent quiz results",
                               bg=bg_colour, fg=font_colour, wrap=250,
                               font=("Comic Sans MS", "12"), justify=LEFT)
        self.help_text.grid(row=1, padx=10)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  bg=bg_colour, fg=font_colour,
                                  font=("Comic Sans MS", "14"),
                                  command=self.close_help)
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self):
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Quiz")
    something = Welcome()
    root.mainloop()
