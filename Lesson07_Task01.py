"""
Home-task 07 Integers to english words

# Convert a non-negative integer num to its English words representation.
# Example 1:
# Input: num = 123
# Output: "One Hundred Twenty Three"

# let's take that number always > 100 and only three digits
# 100 <= num <= 999
"""


def numbertowords(num):
    ones = ['', 'One', 'Two', 'Three', 'Four', 'Five',
            'Six', 'Seven', 'Eight', 'Nine']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty',
            'Sixty', 'Seventy', 'Eighty', 'Ninety']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
             'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

    num_str = str(num)
    length = len(num_str)

    if length == 3:
        return ones[int(num_str[0])] + ' Hundred ' + numbertowords(int(num_str[1:]))

    if length >= 2:
        if num_str[0] == '1':
            return teens[int(num_str[1])]
        else:
            return tens[int(num_str[0])] + ' ' + numbertowords(int(num_str[1:]))

    return ones[int(num_str)]


# Test the function
num = 234
result = numbertowords(num)
print(result)
