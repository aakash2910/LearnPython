# with parenthesis
numbers = (10,20,30)
print(type(numbers))

# without parenthesis
numbers = 10,20,30
print(type(numbers))

# homogeneous type
alphaNumeric = (10,20,'A','B')
print(type(alphaNumeric))

# tuple is mutable hence you get TypeError
# when you try to make changes
numbers[0] = 40
print(numbers)
