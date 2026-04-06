# x=2
# y=3
# z=3
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y)
# print(x**y)
# print(x//y)

# p = x + (y * z)
# print(p)

# import math
# print(math.floor(3.7))  # Output: 3
# print(math.ceil(3.2))   # Output: 4
# print(math.floor(-3.7)) # Output: -4
# print(math.ceil(-3.2))  # Output: -3
# print(math.trunc(3.7))  # Output: 3
# print(math.trunc(-3.7)) # Output: -3

print(0o20)  # Output: 16
print(0x20)  # Output: 32   
print(0b1010)  # Output: 10

print(oct(16))  # Output: '0o20'
print(hex(32))  # Output: '0x20'    
print(bin(10))  # Output: '0b1010'

print(int('0o20', 8))  # Output: 16
print(int('0x20', 16)) # Output: 32 
print(int('0b1010', 2)) # Output: 10

x = 1
print(x << 2)  # Output: 4 (1 shifted left by 2 bits)
print(x >> 1)  # Output: 0 (1 shifted right by 1 bit)

import random
print(random.randint(1, 100))  # Output: A random integer between 1
print(random.choice(['apple', 'banana', 'cherry']))  # Output: A random choice from the list    

l1 = [1,2,3,4,5]
print(random.choice(l1))  # Output: A random choice from the list l1

print(random.shuffle(l1))  # Output: None (the list l1 is shuffled in place)

# here when we work with decimal places we can get some unexpected results due to the way floating-point numbers are represented in memory. This is a common issue in many programming languages, including Python.
print(0.1 + 0.2)  # Output: 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # Output: False
print(0.1 + 0.2 - 0.3)  # Output: 5.551115123125783e-17

# so for more accurate decimal arithmetic, you can use the `decimal` module in Python, which provides a `Decimal` data type for decimal floating-point arithmetic. Here's how you can use it:
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # Output: 0.3
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))  # Output: True
print(Decimal('0.1') + Decimal('0.2') - Decimal('0.3'))  # Output: 0E-17 (which is effectively zero)    

from fractions import Fraction
print(Fraction(1,3) + Fraction(1,6))  # Output: 1/2

set1 = {1,2,3,4,5}
set2 = {1,3,5,7,9}

print(set1 & set2 )  # Output: {1, 3, 5} (intersection)
print(set1 | set2 )  # Output: {1, 2, 3, 4, 5, 7, 9} (union)

print(set1 - set2)  # Output: {2, 4} (difference)
print(set1 ^ set2)  # Output: {2, 4, 7, 9} (symmetric difference)

print(type(set()))  # Output: <class 'set'>
print(type({}))  # Output: <class 'dict'> (empty curly braces create a dictionary, not a set)

print(type(True))  # Output: <class 'bool'>
print(type(False))  # Output: <class 'bool'>