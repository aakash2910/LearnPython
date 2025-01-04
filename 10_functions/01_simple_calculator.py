def add(numOne, numTwo):
    return numOne+numTwo

def sub(numOne, numTwo):
    return numOne-numTwo

def mul(numOne, numTwo):
    return numOne*numTwo

def div(numOne, numTwo):
    if numOne and numTwo != 0:
        return numOne / numTwo
    else:
        print("Please enter values other than zero.")

print(add(10,20))
print(sub(10,20))
print(mul(10,20))
print(div(0,10))
print(div(10,0))
print(div(10,20))

