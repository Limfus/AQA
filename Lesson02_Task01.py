poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze. 

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

"""Create a dictionary to store the vowel counts"""

vowel_counts = {
    'A': 0,
    'E': 0,
    'I': 0,
    'O': 0,
    'U': 0
}

"""Iterate through each character in the poem text"""

for char in poem_text:
    """ Convert the character to uppercase for comparison"""
    char = char.upper()

    """Check if the character is a vowel"""
    if char in vowel_counts:
        vowel_counts[char] += 1

"""Print the table header"""
print("-----------------")
print("| Vowel | Count |")
print("-----------------")

"""Print the vowel counts"""
for vowel, count in vowel_counts.items():
    print(f"|   {vowel}   |   {count}   |")

"""Print the table footer"""
print("-----------------")

"""Modify the text by replacing each vowel
 with the specified character"""

modified_text = poem_text.replace('A', 'À').replace('a', 'à') \
    .replace('E', 'É').replace('e', 'é') \
    .replace('I', 'Í').replace('i', 'í') \
    .replace('O', 'Ó').replace('o', 'ó') \
    .replace('U', 'Ú').replace('u', 'ú')

"""Print the modified text"""

print(modified_text)

