
def factorial(number):
    result = 1
    while(number > 0):
        result = result * number
        number -= 1
    return result

input = eval(input("Enter the number : "))
print("Factorial of {} is : ".format(input), factorial(input))

# using factorial
def recursiveFactorial(number):
    if number == 1:
        return number
    else:
        return number * recursiveFactorial(number-1)
print("Factorial of {} is : ".format(input), recursiveFactorial(input))