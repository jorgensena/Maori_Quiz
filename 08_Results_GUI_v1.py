"""
Make the Results GUI

By Amy Jorgensen
22/05/22
"""
from tkinter import *
from functools import partial


class Welcome:
    def __init__(self):

        # formatting variables
        bg_colour = "#FFF4D9"  # pale yellow
        font_colour = "#990000"  # dark red
        btn_colour = "#FFFFCC"  # pale yellow

        # Quiz Main Screen GUI
        self.main_frame = Frame(width=300, height=300, bg=bg_colour)
        self.main_frame.grid()

        # Maori Quiz Heading (row 0)
        self.maori_main_label = Label(self.main_frame, text="Maori Quiz",
                                      font=("Comic Sans MS", "30", "bold",
                                            "underline"),
                                      bg=bg_colour, fg=font_colour,
                                      padx=10, pady=10)
        self.maori_main_label.grid(row=0)

        # Quiz button (row 1)
        self.quiz_button = Button(self.main_frame, text="Start Quiz",
                                  font=("Comic Sans MC", "14"),
                                  padx=10, pady=10, bg="#D5E8D4",  # green
                                  fg=font_colour, command=self.quiz)
        self.quiz_button.grid(row=1)

        # Button frame (row 2) (for help and welcome btns)
        self.main_button_frame = Frame(self.main_frame, bg=bg_colour)
        self.main_button_frame.grid(row=2)

        # Help Button (row 0)
        self.help_button = Button(self.main_button_frame, text="Help",
                                  font=("Comic Sans MC", "14"),
                                  padx=10, pady=10, bg=btn_colour,
                                  fg=font_colour, command=self.help)
        self.help_button.grid(row=0, column=0, pady=10, padx=10)
        # results Button (row 1)
        self.results_button = Button(self.main_button_frame, text="Results",
                                  font=("Comic Sans MC", "14"),
                                  padx=10, pady=10, bg=btn_colour,
                                  fg=font_colour, command=self.results)
        self.results_button.grid(row=0, column=1, pady=10, padx=10)

    def results(self):
        print("You asked for results")
        Results(self)

    def help(self):
        print("You asked for help")

    def quiz(self):
        print("You want to do the quiz")


class Results:
    def __init__(self, partner):
        # formatting variables
        bg_colour = "#FFF4D9"  # pale yellow
        font_colour = "#990000"  # dark red
        btn_colour = "#FFFFCC"  # pale yellow

        # disable results button
        partner.results_button.config(state=DISABLED)

        # set up child window
        self.results_box = Toplevel()

        # If user uses cross to exit, results button is enabled
        self.results_box.protocol("WM_DELETE_WINDOW", partial(self.close_results,
                                                           partner))

        # set up GUI frame
        self.results_frame = Frame(self.results_box, width=300, bg=bg_colour)
        self.results_frame.grid()

        # set up results heading (row 0)
        self.results_heading = Label(self.results_frame, text="Results",
                                  font=("Comic Sans MS", "30", "bold",
                                        "underline"),
                                  bg=bg_colour, fg=font_colour)
        self.results_heading.grid(row=0)

        # results text (row 1)
        self.results_text = Label(self.results_frame,
                               text="Scores:", bg=bg_colour, fg=font_colour,
                               font=("Comic Sans MS", "14", "underline"))
        self.results_text.grid(row=1, padx=10, pady=10)

        # Button frame for 'Dismiss' and 'Export' btns (row 3)
        self.results_btn_frame = Frame(self.results_frame, bg=bg_colour)
        self.results_btn_frame.grid(row=3)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.results_btn_frame, text="Dismiss",
                                  bg=btn_colour, fg=font_colour,
                                  font=("Comic Sans MS", "14"),
                                  command=partial(self.close_results, partner))
        self.dismiss_btn.grid(row=0, column=0, pady=10, padx=10)

        # Export button (row 2)
        self.export_btn = Button(self.results_btn_frame, text="Export",
                                  bg=btn_colour, fg=font_colour,
                                  font=("Comic Sans MS", "14"))
        self.export_btn.grid(row=0, column=1, pady=10, padx=10)

    def close_results(self, partner):
        # Put results button back to normal
        partner.results_button.config(state=NORMAL)
        self.results_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Quiz")
    something = Welcome()
    root.mainloop()
