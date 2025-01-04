records = {}

for number in range(0,4):
    name = input("Enter name of the student : ")
    grade = input("Enter grade(A,B,C) : ")
    records[name] = grade

print(records)