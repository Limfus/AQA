import re
"""
Home-task 09 Files operations
# Write script that will read "input.txt" file
and find there all characters from english alphabet
# collect these characters and their positions in file
# after info collected this info as text
write to "output.txt" file in such format
# ####################
# <first found letter> -> pos1
# <next_letter> -> pos2
# <next_letter -> pos3
# etc
# #######################
"""

import re

# Read the input file
with open("input.txt", "r") as input_file:
    # Read the contents of the file
    content = input_file.read()

# Find all English alphabet characters and their positions
letter_positions = [(match.group(), match.start() + 1)
                    for match in re.finditer(r"[A-Za-z]", content)]

# Write the collected information to the output file
with open("output.txt", "w") as output_file:
    # Write the header
    output_file.write("#########################\n")

    # Write the characters and their positions
    for letter, position in letter_positions:
        output_file.write(f"{letter} -> pos{position}\n")

    # Write the footer
    output_file.write("#########################")
