"""
We have four values w,x,y,z
write if-elif-else statement
that will search minimum value
and print smth aka "'y' is minimum value'
advice use python debugger
and different values to check your algorithm
"""
w, x, y, z = 100, 200, 40, 300

if y <= w and y <= x and y <= z:
    print("'y' is the minimum value.")
elif w <= x and w <= y and w <= z:
    print("'w' is the minimum value.")
elif x <= w and x <= y and x <= z:
    print("'x' is the minimum value.")
else:
    print("'z' is the minimum value.")
