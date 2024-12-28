number = int(input("Enter the number: "))
asciiNum = 65

for num in range(number):
    print(str(chr(num + asciiNum) + ' ') * number)