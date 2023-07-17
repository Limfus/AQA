import re

# Read the input file
with open("example.txt", "r") as input_file:
    # Read the contents of the file
    content = input_file.read()

# Find all English alphabet characters and their positions
found_letters = re.findall(r"[A-Za-z]", content)
letter_positions = [(char, content.index(char) + 1) for char in found_letters]

# Write the collected information to the output file
with open("output.txt", "w") as output_file:
    # Write the header
    output_file.write("#########################\n")

    # Write the characters and their positions
    for letter, position in letter_positions:
        output_file.write(f"{letter} -> pos{position}\n")

    # Write the footer
    output_file.write("#########################")
