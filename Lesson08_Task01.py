"""
Home-task 08 Max three multiplication
# Given the list of integers ( positive , negative, zeros)
# Find max multiplication of three values in list
l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

# Input: [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]
# Output: Max value = "360". Nums are: (12, 5, 6)

# Input: [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
# Output: Max value = "2016". Nums are: (-7, 12, -24)
"""


l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

sorted_list = sorted(l1)
max_product = sorted_list[-1] * sorted_list[-2] * sorted_list[-3]
min_product = sorted_list[0] * sorted_list[1] * sorted_list[-1]

max_multiplication = max(max_product, min_product)
print("Max value =", max_multiplication)

