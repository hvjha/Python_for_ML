mylist = [1,2,3,['a','b','c']]
print(mylist[0])
print(mylist[3])
print(mylist[3][0])

print(2**10)
print(2**1000)

import math
print(math.sqrt(16)) 

import random
print(random.randint(1,100))
print(random.choice(['apple','banana','cherry']))

username = "hitesh"
print(len(username))
print(username[0])
# username[0] = 'H'  # This will raise an error because strings are immutable
print(username[0].upper() + username[1:])  # This will create a new string with the first letter capitalized
print(username[1:3])

mylist = [1,2,3,4,5]
print(mylist[0])

mydict = {'name': 'hitesh', 'age': 30, 'city': 'delhi'}
print(mydict['name'])

myTuple = (1,2,3,4,5)
print(myTuple[0])