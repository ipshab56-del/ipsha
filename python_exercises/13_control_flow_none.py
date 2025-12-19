# Exercise 13: None Exercise
# Given the variables x, y, and z, print the sum of the values that are not None.

x = 10
y = None
z = 20

total = 0

if x is not None:
    total += x

if y is not None:
    total += y

if z is not None:
    total += z

print(f"Sum of non-None values: {total}")
