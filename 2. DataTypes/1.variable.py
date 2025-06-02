# Python variable naming conventions and types

# Data types in Python
data_types = {
    "int": 42,
    "float": 3.14,
    "str": "Hello, World!",
    "bool": True,
    "list": [1, 2, 3],
    "tuple": (1, 2, 3),
    "set": {1, 2, 3},
    "dict": {"name": "Bapu", "age": 25},
    "complex": complex(1, 2),
    "bytes": bytes(5),
    "bytearray": bytearray(5),
    "frozenset": frozenset([1, 2, 3]),
}
# Printing the data types and their values
for data_type, value in data_types.items():
    print(f"{data_type}: {value} (type: {type(value)})")


# Python variable
# A variable is a container for storing data values.
# In Python, variables do not need to be declared with a specific type.

# Variable declaration and type checking in Python
# Variables in Python are created when you assign a value to them.
# Variable names can contain letters, numbers, and underscores, but cannot start with a number.
# Variable names are case-sensitive, meaning that 'myVar' and 'myvar' are considered different variables.

# Valid variable names:
myVar = 5       # Valid
my_variable = 15  # Valid
myVar3 = 25      # Valid
_myVar = 20      # Valid


# Invalid variable names:
# 1myVar = 35    # Invalid: cannot start with a number
# class = 45     # Invalid: 'class' is a reserved keyword
# my-var = 55   # Invalid: cannot contain hyphens
my_var = 10      # Valid
myVar2 = 30      # Valid


# what happens when we try to declare a variable
s =10 # this stores 3 information in the variable s in memory
# 1. reference count (how many references point to this variable)
#    (1 in this case, since it's the only reference)
# 2. The value of the variable (10)
# 3. The type of the variable (int)

print("type of s: ", type(s)) # this will print the type of the variable s
print("id of s: ", id(s)) # this will print the memory address of the variable s
print("value of s: ", s) # this will print the value of the variable s

# Now let's declare a new variable t with the same value as s
t = 10  # this creates a new variable t with the same value as s
print("type of t: ", type(t))  # this will print the type of the variable t
print("id of t: ", id(t))  # this will print the memory address of the variable t which is same as s
print("value of t: ", t)  # this will print the value of the variable t

# how to check what are the reserve keywords present in python
help("keywords")  # this will print the list of reserved keywords in python
