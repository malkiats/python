# Import the entire module:
import math
print(math.sqrt(16))  # Output: 4.0


# Import specific functions or variables:
from math import sqrt
print(sqrt(16))  # Output: 4.0

# Import with an alias:
import math as m
print(m.sqrt(16))  # Output: 4.0

# Import all functions (not recommended due to namespace pollution):
from math import *
print(sqrt(16))  # Output: 4.0


###############################
# Example:
'''
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b


# main.py
import mymodule

print(mymodule.greet("Alice"))  # Output: Hello, Alice!
print(mymodule.add(5, 3))       # Output: 8
'''


