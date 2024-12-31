a = 10
b = 20
c = 30
d = 40

# packing tuple
numbers = a,b,c,d
print(numbers)
print(type(numbers))

# unpacking tuple
numOne, numTwo, numThree, numFour = numbers
print(numOne, numTwo, numThree, numFour)

numOne, *numTwo = numbers
print(numOne, numTwo)

