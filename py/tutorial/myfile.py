### Python Tutorial Notes

print("5 > 2")
if 5 > 2:
    print("Five is greater than two!")

x = 5
y = "Hello, world!"

print ("\nVariables")
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

print("\nVariables")
def myfunc():
    print("Python is " + y)

myfunc()

print("\nInside")
def myfuncinside():
    y = "cool"
    print("Python is " + y)

myfuncinside()
print("\nGlobal")
def myfuncglobal():
    global m
    m = "inside"

myfuncglobal()

print("Python is " + m)

m = "outside"

myfuncglobal()

print("Python is " + m)

x = 5
print(type(x))

integernum = 1
floatnum = 2.8
complexnum = 1j

print(type(integernum))
print(type(floatnum))
print(type(complexnum))

ina = float(integernum)
flb = float(floatnum)
coa = float(integernum)

print(ina)
print(flb)
print(coa)

import random
print("\nRandom")
print(random.randrange(1,10))

multiline_doublequotes = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

multiline_singlequotes = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print("\ndouble quotes\n" + multiline_doublequotes)

print("\nsingle quotes\n" + multiline_singlequotes)

print("\nstring array")
a = "\nHello, world!"
print(a[1])

print("\Looping string array")
for x in "banana":
    print(x)

print("len function\n",len(a))


print("\ncheck string")
txt = "The best things in life are free!"
print(txt)
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

print("\nslicing")
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
