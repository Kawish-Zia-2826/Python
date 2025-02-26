# print("this is first hello worls program")
#var in python
a = 10
b = "stirng"
c = 10.5
# python comment
"""python multi line commnet"""
# casting in python
x = int(1)
b = str("sbc")
c = float(1.5)
# pyhton get type
print(type(x))
# python string can be deaclared with single or double quotes
a = "hello"
b = 'hello'
# python case sensative
a = 4
A = "s"


""" A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords."""


# python camel case
myVariableName = "John"
# python pascal case
MyVariableName = "John"
# python snake case
my_variable_name = "John"

# many values to mutiple variables
# python allow you to assign values to multiple variables in one line
a, b, c = "orange", "banana", "cherry"


# Note: Make sure the number of variables matches the number of values, or else you will get an error.

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line
x=y=z = "orange"

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits


# Output Variables
g = "awesome"

def myfunc():
  g = "fantastic"
print("Python is " + g)

myfunc()


import random
print(random.randrange(1, 10))


print(len("kawish"))
name = "abcd efg"
if "abcdsdf"not  in name:
    print("true")


for x in name:
  print(x.upper())

  price   = 10

  print(f"the price of {price:.2f}")

