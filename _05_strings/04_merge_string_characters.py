stringOne = "aakash"
stringTwo = "ravi"

minLength = len(stringOne) if len(stringOne) < len(stringTwo) else len(stringTwo)
newString = ""

for index in range(0,minLength):
    newString = newString + stringOne[index] + stringTwo[index]

newString = newString + stringOne[4:]

print(newString)

