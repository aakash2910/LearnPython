number = int(input("Enter the number : "))

for i in range(number,0,-1):
    for j in range(i):
        print("* ", end="")
    print()

for i in range(number, 0, -1):
    print("* " * (number - i))
