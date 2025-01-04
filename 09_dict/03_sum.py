points = eval(input("Enter the names as the keys and associated points as values : "))
sumOfPoints = 0
for value in points.values():
    sumOfPoints += value

print(sumOfPoints)

#using sum()
print(sum(points.values()))