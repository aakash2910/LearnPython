stringOne = "LISTEN"
stringTwo = "SILENT"

if len(stringOne) != len(stringTwo):
    print("Both strings are not anagram")

else:
    if sorted(stringOne) == sorted(stringTwo):
        print("Both strings are anagrams")
    else:
        print("Both strings are not anagrams")
