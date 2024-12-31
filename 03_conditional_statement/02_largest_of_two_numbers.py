first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

if(first_number > second_number):
    print("{} is the largest.".format(first_number))
elif(first_number < second_number):
    print("{} is the largest".format(second_number))
else:
    print("Both {} and {} are equal.".format(first_number, second_number))
    