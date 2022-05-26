"""
Check the filenames are valid
Includes RegEx to check filename is valid (A-Z a-z 0-9 and underscores)
Export lists to file

By Amy Jorgensen
24/05/22
"""

import re


def get_filename(question):
    has_error = "yes"
    error_type = ""
    while has_error == "yes":
        print()
        filename = input(question)
        has_error = "no"

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
            print(f"Invalid filename - {error_type}")
        else:
            print("You entered a valid filename")
            return filename + ".txt"


def export(filename, data):
    # Create file to hole data
    f = open(filename, "w+")

    for item in data:
        f.write(item + "\n")

    # close file
    f.close()


# Main routine
# Data to be outputted
scores = ["1/3", "2/3", "1/3", "2/3", "3/3", "3/3"]
wrong = ["What is Tahi", "What is Rua", "What is Rua", "What is Tahi",
         "What is Toru", "What is Toru"]

# export scores data
export(get_filename("Enter a filename for the scores file: "), scores)
# export questions wrong data
export(get_filename("Enter a filename for the questions wrong file: "), wrong)
