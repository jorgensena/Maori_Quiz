"""
Check the filenames are valid
Includes RegEx to check filename is valid (A-Z a-z 0-9 and underscores)

By Amy Jorgensen
24/05/22
"""

import re


has_error = "yes"
error_type = ""
while has_error == "yes":
    print()
    filename = input("Enter a filename: ")
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

