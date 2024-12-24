# Sum of two numbers

numberOne = input("Enter first number : ")
numberTwo = input("Enter second number : ")
print("Sum of two numbers is : ", (int(numberOne) + int(numberTwo)))

# Multiplication of two numbers
print("Multiplication of two numbers is : ", (int(numberOne) * int(numberTwo)))

# Division of two numbers
print("Division of two numbers is : ", (int(numberOne) / int(numberTwo)))

# Take 3 values from user in single line and print sum of those entered values
a,b = [ int(x) for x in input("Enter two numbers : ").split()]
print("Sum is : ", a+b)