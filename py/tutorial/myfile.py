if 5 > 2:
    print("Five is greater than two!")

x = 5
y = "Hello, world!"

print (x, y)

### comment

"""
multiline comment
"""

### casting
s = str(3)  # x is '3'
i = int(3)  # y is 3
f = float(3) # f is 3.0

print (s, i, f)

print(type(s))
print(type(i))
print(type(f))

def myfunc():
    print("Python is " + y)

myfunc()

def myfuncinside():
    y = "cool"
    print("Python is " + y)

myfuncinside()

def myfuncglobal():
    global m
    m = "inside"

myfuncglobal()

print("Python is " + m)

m = "outside"

myfuncglobal()

print("Python is " + m)
