# Exercise 14: Boolean Operations Exercise
# Given the variables x, y, and z print the following:
# 1. if x and y are greater than 10, print 'step 1 is True'
# 2. if z or y is greater than x, print 'step 2 is True'
# 3. if step 2 is False, print 'step 2 is False'

x = 15
y = 12
z = 5

# Step 1
if x > 10 and y > 10:
    print("step 1 is True")

# Step 2
if z > x or y > x:
    print("step 2 is True")
else:
    print("step 2 is False")
