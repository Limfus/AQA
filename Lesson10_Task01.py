"""
Home-task Regex

# open input.txt file and find all small
 english letters that match such conditions:
# target small letter round exactly with
 three capital english letters on the left and on the right
# Match examples:
# sdTRYaUVKn  -> matches "a"
# NTRSjARTb   -> no match ( not exactly 3 capital letters on the left)
# zDFGbOPNq   -> matches "b"
# Print Output as : "Result: "<your_found_human_readable_string">
"""

import re

# Read the input file
with open("input02.txt", "r") as input_file:
    # Read the contents of the file
    content = input_file.read()

# Find all small English letters that match the specified conditions
matches = re.findall(r'(?<=[A-Z]{3})([a-z])(?=[A-Z]{3})', content)

# Convert the matches to a human-readable string
result_string = "".join(matches) if matches else "No matches found"

# Print the result
print(f"Result: \"{result_string}\"")
