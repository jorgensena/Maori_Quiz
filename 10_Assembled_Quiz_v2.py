"""
Putting the components together to make a full working program
Add in a scoring system which then display a final score at the end of the quiz
Disable the check button after a question is marked

By Amy Jorgensen
30/05/22
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

        self.all_scores = []
        self.all_wrong = []

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
                                  fg=font_colour,
                                  command=lambda: self.quiz(self.all_scores,
                                                            self.all_wrong))
        self.quiz_button.grid(row=1)

        # Button frame (row 2) (for help and welcome btns)
        self.main_button_frame = Frame(self.main_frame, bg=bg_colour)
        self.main_button_frame.grid(row=2)

        # Help Button (row 0)
        self.help_button = Button(self.main_button_frame, text="Help",
                                  font=("Comic Sans MC", "14"),
                                  padx=10, pady=10, bg=btn_colour,
                                  fg=font_colour, command=self.help)
        self.help_button.grid(column=0, pady=10)

        # results Button (row 1)
        self.results_button = Button(self.main_button_frame, text="Results",
                                     font=("Comic Sans MC", "14"), padx=10,
                                     pady=10, bg=btn_colour, fg=font_colour,
                                     command=lambda: self.results(
                                         self.all_scores, self.all_wrong))
        self.results_button.grid(row=0, column=1, pady=10, padx=10)

    def help(self):
        print("You asked for help")
        Help(self)

    def quiz(self, all_scores, all_wrong):
        print("You want to do the quiz :)")
        Quiz(self, all_scores, all_wrong)

    def results(self, all_scores, all_wrong):
        print("You asked for results")
        Results(self, all_scores, all_wrong)


class Quiz:
    def __init__(self, partner, all_scores, all_wrong):

        # formatting variables
        bg_colour = "#FFF4D9"  # pale yellow
        font_colour = "#990000"  # dark red
        btn_colour = "#FFFFCC"  # pale yellow

        self.counter = 0
        self.quiz_score = 0
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
                                    text="Click Start to begin :)",
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
                                   command=lambda: self.check_question(all_scores, all_wrong))
        self.check_button.grid(row=0, column=0, padx=5, pady=10)
        self.check_button.config(stat=DISABLED)

        # 'Next' button (column 0)
        # When window opens says Start to start the quiz
        self.next_button = Button(self.quiz_button_frame, text="Start",
                                  font=("Comic Sans MS", "14"),
                                  bg="#D4E1F5",  # pale blue
                                  fg=font_colour,
                                  command=self.next_question)
        self.next_button.grid(row=0, column=1, padx=5, pady=10)

        # Dismiss button (row 5)
        self.dismiss_button = Button(self.quiz_frame, text="Dismiss",
                                     font=("Comic Sans MS", "14"),
                                     bg=btn_colour, fg=font_colour,
                                     command=partial(self.close_quiz, partner))
        self.dismiss_button.grid(row=5, pady=10)

    # Method to check question
    def check_question(self, all_scores, all_wrong):
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
                    self.check_button.config(state=DISABLED)
                    self.quiz_score += 1  # add a point as correct
                else:
                    self.message_label.config(fg=font_colour,
                                              text="Oops! That was incorrect")
                    self.check_button.config(state=DISABLED)
                    all_wrong.append(f"What is {self.question[0]}")

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
                self.check_button.config(state=DISABLED)
                self.quiz_score += 1  # add a point as correct
            elif not to_check:
                self.message_label.config(text="You left it blank!",
                                          fg="black")
                self.question_entry.config(bg=error)
                has_errors = True
            else:
                self.question_entry.config(bg="white")
                self.message_label.config(fg=font_colour,
                                          text="Oops! That was incorrect")
                self.check_button.config(state=DISABLED)
                all_wrong.append(f"What is {self.question[1]}")
        if not has_errors and self.counter != 10:
            self.next_button.config(state=NORMAL)

        if self.counter == 10:
            self.question_label.config(text=f"End of Quiz "
                                            f"\n{self.quiz_score}/10")
            all_scores.append(f"{self.quiz_score}/10")
        print(self.quiz_score)  # print for testing purposes

    # Method to change the quiz_label to show the next question
    def next_question(self):
        self.next_button.config(text="Next")
        self.check_button.config(state=NORMAL)
        self.message_label.config(text="Write your answer below")
        self.question_entry.delete(0, END)
        # the quiz is 10 questions
        if self.counter != 10:
            self.question, self.q_num_list = next_q(self.maori_q,
                                                    self.q_num_list)
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


class Help:
    def __init__(self, partner):
        # formatting variables
        bg_colour = "#FFF4D9"  # pale yellow
        font_colour = "#990000"  # dark red

        # disable help button
        partner.help_button.config(state=DISABLED)

        # set up child window
        self.help_box = Toplevel()

        # If user uses cross to exit, help button is enabled
        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help,
                                                           partner))

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
                               text="\nThis is a quick 10 question quiz on "
                                    "Maori numbers (1-10). You could be asked "
                                    "to translate from Maori to integer, or "
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
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


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
        self.results_box.protocol("WM_DELETE_WINDOW", partial(
            self.close_results, partner))

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
                scores_string += all_scores[len(all_scores) - item - 1] + "\n"

        elif len(all_scores) >= 1:
            for item in all_scores:
                scores_string += all_scores[len(all_scores) -
                                            all_scores.index(item) - 1] + "\n"
        else:
            scores_string = "You have not completed a quiz yet"
        # Display scores history
        self.scores_label = Label(self.results_frame,
                                  text="Scores:\n" + scores_string,
                                  bg=bg_colour, fg=font_colour,
                                  font=("Comic Sans MS", "12"), justify=CENTER)
        self.scores_label.grid(row=2)

        # Display most recent wrong question
        if len(all_wrong) == 0:
            last_wrong = "You do not have a question wrong yet"
        else:
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

        # if users press cross at top, close export and 'release' export button
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
                                      command=partial(lambda: self.save_results
                                      (partner, all_scores)))
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
