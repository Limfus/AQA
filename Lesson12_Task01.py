"""
Home-task 12 Recursion

Given list of list of list etc of integers
write recursive function that will accept as argument target list
and return sum of all integers inside it
Input: [[[[1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
Output: Target sum = 72
"""


def iterative_integer_generator(target_list):
    stack = [target_list]
    while stack:
        current_item = stack.pop()
        if isinstance(current_item, int):
            yield current_item
        elif isinstance(current_item, list):
            stack.extend(reversed(current_item))


def get_target_sum(target_list):
    integer_iterator = iterative_integer_generator(target_list)
    target_sum = sum(integer_iterator)
    return target_sum


# Test the function with the given input
input_list = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
output_sum = get_target_sum(input_list)
print("Target sum =", output_sum)  # Output: Target sum = 72
