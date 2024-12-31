numbers = [1,2,3,4,5,6,7,8,9,10]

#using for loop
for number in numbers:
    print(str(number) + " ", end="")
print()

#using while loop
i = 0
while(i < len(numbers)):
    print("{} ".format(numbers[i]), end="")
    i += 1