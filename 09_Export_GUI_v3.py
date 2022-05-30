"""
Make the Export GUI
Add in method to save data to file
- Saves only scores and closes export GUI when complete

By Amy Jorgensen
26/05/22
"""
from tkinter import *
from functools import partial
import re


class Welcome:
    def __init__(self):

        # formatting variables
        bg_colour = "#FFF4D9"  # pale yellow
        font_colour = "#990000"  # dark red
        btn_colour = "#FFFFCC"  # pale yellow

        # Data to be outputted
        self.all_scores = ["1/3", "2/3", "1/3", "2/3", "3/3", "3/3"]
        self.all_wrong = ["What is Tahi?", "What is Rua?", "What is Rua?",
                          "What is Tahi?", "What is Toru?", "What is Toru?"]

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
                                     font=("Comic Sans MC", "14"), padx=10,
                                     pady=10, bg=btn_colour, fg=font_colour,
                                     command=lambda: self.results(
                                         self.all_scores, self.all_wrong))
        self.results_button.grid(row=0, column=1, pady=10, padx=10)

    def results(self, all_scores, all_wrong):
        print("You asked for results")
        Results(self, all_scores, all_wrong)

    def help(self):
        print("You asked for help")

    def quiz(self):
        print("You want to do the quiz")


class Results:
    def __init__(self, partner, all_scores, all_wrong):
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
                                  text="Here are your most recent scores and "
                                       "last question answered wrong."
                                       "\nUse the export button to create text"
                                       " files of this sessions results. One "
                                       "file for scores, and one file for the "
                                       "questions answered wrong",
                                  bg=bg_colour, fg=font_colour, wrap=250,
                                  justify=LEFT, width=30,
                                  font=("Comic Sans MS", "12"))
        self.results_text.grid(row=1, padx=10, pady=10)

        # Get results
        scores_string = ""
        if len(all_scores) >= 5:
            for item in range(5):
                scores_string += all_scores[len(all_scores)-item-1]+"\n"

        else:
            for item in all_scores:
                scores_string += all_scores[len(all_scores) -
                                            all_scores.index(item)-1]+"\n"

        # Display scores history
        self.scores_label = Label(self.results_frame,
                                  text="Scores:\n" + scores_string,
                                  bg=bg_colour, fg=font_colour,
                                  font=("Comic Sans MS", "12"), justify=CENTER)
        self.scores_label.grid(row=2)

        # Display most recent wrong question
        last_wrong = all_wrong[-1] + "\n"
        self.wrong_label = Label(self.results_frame,
                                 text="Last got Wrong:\n" + last_wrong,
                                 bg=bg_colour, fg=font_colour,
                                 font=("Comic Sans MS", "12"), justify=CENTER)
        self.wrong_label.grid(row=3)

        # Button frame for 'Dismiss' and 'Export' btns (row 4)
        self.results_btn_frame = Frame(self.results_frame, bg=bg_colour)
        self.results_btn_frame.grid(row=4)

        # Export button (row 2)
        self.export_btn = Button(self.results_btn_frame, text="Export",
                                 bg=btn_colour, fg=font_colour,
                                 font=("Comic Sans MS", "14"),
                                 command=lambda: self.export(all_scores))
        self.export_btn.grid(row=0, column=0, pady=10, padx=10)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.results_btn_frame, text="Dismiss",
                                  bg=btn_colour, fg=font_colour,
                                  font=("Comic Sans MS", "14"),
                                  command=partial(self.close_results, partner))
        self.dismiss_btn.grid(row=0, column=1, pady=10, padx=10)

    def close_results(self, partner):
        # Put results button back to normal
        partner.results_button.config(state=NORMAL)
        self.results_box.destroy()

    def export(self, all_scores):
        print("You want to export")
        Export(self, all_scores)


class Export:
    def __init__(self, partner, all_scores):
        # formatting variables
        bg_colour = "#FFF4D9"  # pale yellow
        font_colour = "#990000"  # dark red
        btn_colour = "#FFFFCC"  # pale yellow

        # disable export button
        partner.export_btn.config(state=DISABLED)

        # sets up child window (ie. export box)
        self.export_box = Toplevel()

        # if users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                             partner))

        # set up GUI frame
        self.export_frame = Frame(self.export_box, width=300, bg=bg_colour)
        self.export_frame.grid()

        # set up export heading (row 0)
        self.export_heading = Label(self.export_frame,
                                    text="Export instructions",
                                    font=("Comic Sans MS", "20", "bold",
                                        "underline"),
                                    bg=bg_colour, fg=font_colour)
        self.export_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a filename in the box below and "
                                      "press the Save button to save your "
                                      "scores history to a text file.",
                                 justify=CENTER, width=30, wrap=250,
                                 bg=bg_colour, fg=font_colour,
                                 font=("Comic Sans MS", "12"))
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.warning_text = Label(self.export_frame,
                                  text="If the filename you enter below "
                                       "already exists, it's contents will be "
                                       "replaced with your score results",
                                  justify=LEFT, bg="#ebc091",  # orange
                                  font=("Comic Sans MS", "10"), fg="black",
                                  wrap=225, padx=10, pady=10)
        self.warning_text.grid(row=2)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message labels (row 4)
        self.save_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=bg_colour)
        self.save_label.grid(row=4)

        # Button frame for save and dismiss btns (row 5)
        self.export_btn_frame = Frame(self.export_frame, bg=bg_colour)
        self.export_btn_frame.grid(row=5, pady=10)

        # Save btn (row 0 of export_btn_frame)
        self.save_scores_btn = Button(self.export_btn_frame, text="Save",
                               bg=btn_colour, fg=font_colour,
                               font=("Comic Sans MS", "14"),
                               command=partial(lambda: self.save_results(
                                   partner, all_scores)))
        self.save_scores_btn.grid(row=0, column=0, padx=10)


        # Dismiss btn (row 6)
        self.dismiss_btn = Button(self.export_btn_frame, text="Dismiss",
                                  bg=btn_colour, fg=font_colour,
                                  font=("Comic Sans MS", "14"),
                                  command=partial(self.close_export, partner))
        self.dismiss_btn.grid(row=0, column=1, padx=10)


    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_btn.config(state=NORMAL)
        self.export_box.destroy()


    def save_results(self, partner, data):
        has_error = "no"
        error_type = ""

        filename = self.filename_entry.get()

        valid_char = "[A-Za-z0-9]"
        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                error_type = "(no spaces allowed)"
            else:
                error_type = f"no {letter}'s allowed"
            has_error = "yes"

        if filename == "":
            error_type = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_label.config(text=f"Invalid filename - {error_type}")
            # Change entry box background to orange
            self.filename_entry.config(bg="#ebc091")
        else:
            # If there are no errors, generate text and file and then close
            # dialogue, Add .txt suffix
            filename = filename + ".txt"

            # Create file to hole data
            f = open(filename, "w+")

            for item in data:
                f.write(item + "\n")

            # close file
            f.close()

            # close Export GUI
            partner.export_btn.config(state=NORMAL)
            self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Quiz")
    something = Welcome()
    root.mainloop()
