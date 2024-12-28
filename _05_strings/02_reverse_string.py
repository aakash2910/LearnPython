string = input("Enter the string : ")
print(string[::-1])

for char in range(len(string)-1,-1,-1):
    print(string[char],end='')


