string = input("Enter any random string: ")
letterCount = {}

for letter in string:
    if letter not in letterCount:
        letterCount[letter] = 1
    else:
        letterCount[letter] = letterCount.get(letter) + 1

print(letterCount)

# Another way
for letter in string:
    letterCount[letter] = letterCount.get(letter, 0) + 1

print(letterCount)