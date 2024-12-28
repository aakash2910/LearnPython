string = "Learning python is very easy"
listOfWords = string.split()

#first way
for word in range(len(listOfWords)-1, -1, -1):
    print(listOfWords[word] + " ", end="")

print()
print(" ".join(listOfWords[::-1]))

#second way
secondWordReversed = ""
for index in range(0,len(listOfWords),1):
    if index % 2 != 0:
        secondWordReversed = secondWordReversed + " " + listOfWords[index][::-1]
    else:
        secondWordReversed = secondWordReversed + " " + listOfWords[index]

print(secondWordReversed.lstrip())















