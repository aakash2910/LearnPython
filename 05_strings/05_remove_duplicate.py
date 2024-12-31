string = "aabbdddcc"
output = ""

#first way
for char in string:
    if char not in output:
        output += char

print(output)

#second way - order is not preserved
print("".join(set(string)))