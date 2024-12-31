numbers = int(input("How many numbers you would like to print from 1 : "))

for number in range(1,numbers+1,2):
    print(str(number) + " ", end='')

# Using while loop
print()
number = 1

while(number <= 10):
    print(str(number) + " ", end='')
    number += 1

