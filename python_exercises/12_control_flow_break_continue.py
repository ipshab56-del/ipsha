# Exercise 12: Break and Continue Exercise
# Given a number x, use continue to print out even numbers from 0 to x. 
# Use break to stop if you reach a number greater than 20.

x = 30

for i in range(x):
    if i > 20:
        break
    if i % 2 != 0:
        continue
    print(i)
