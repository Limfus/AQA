"""
Home-task 06 Comprehensions

ex. l1=[1,3,5,7]  l2=[1,4,5]
task:
create list that will store such values
list_target = [(1,1), (3,4), (5,5), (7,0)]
zero (0) is our default value that we set
if no such element by index was found in certain list.
code should work and vise versa
ex. l1=[1,4,5] l2=[1,3,5,7] input data should produce
list_target = [(1,1), (4,3), (5,5), (0,7)]
your solution should include comprehension constructions
"""

l1 = [2, 4, 6, 8, 10]
l2 = [1, 2, 3]

max_size = max(len(l1), len(l2))

list_target = [(l1[i], l2[i]) if i < len(l1) and i < len(l2) else (l1[i], 0) if i < len(l1) else (0, l2[i]) for i in range(max_size)]

print(list_target)
