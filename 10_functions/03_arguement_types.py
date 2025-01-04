# positional
def add(a, b):
    return a + b

print(add(10,20))

# Keyword
def sub(a, b):
    return a - b

print(sub(b = 20, a = 10))

# Default
def mul(a=0, b=0):
    return a*b

print("Without default values : ",str(mul(10,20)))
print("With default values ", mul())