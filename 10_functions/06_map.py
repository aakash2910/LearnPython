# Add 1 to all elements present in the sequence
numbers = [1,2,3,4,5,6,7,8,9,10]

newNumbers = list(map(lambda number : number + 1, numbers))
print(newNumbers)

# Square of each element present in the sequence
newNumbers = list(map(lambda number : number * number, numbers))
print(newNumbers)