numbers = [1,2,3,4,5,6,7,8,9,10]

# without lambda
def isEven(number):
    if number  % 2 == 0:
        return True
    else:
        return False

evenNumbers = list(filter(isEven, numbers))
print(evenNumbers)

#with lambda
evenNumbersWithLambda = list(filter(lambda number : number%2 == 0, numbers))
print(evenNumbersWithLambda)