mylist = ["Hitesh", "Python", "Programming", 2024]
print(mylist)
print(mylist[0])
print(mylist[1:3])
print(mylist[:2])
print(mylist[:])
print(mylist[1:4:2])
print(mylist[2:])
mylist.append("New Item")
print(mylist)
mylist.insert(2,"Java")
print(mylist)
mylist.remove(2024)
mylist.insert(4,"C++")
mylist.append("JavaScript")
print(mylist)
mylist.pop()
print(mylist)
mylist.pop(2)
print(mylist)
mylist.reverse()
print(mylist)
mylist.sort()
print(mylist)
mylist[3] = "Django"
print(mylist)
mylist[1:3] = ["Flask", "Data Science"]
print(mylist)
mylist[1:2] = "AI"
print(mylist)
mylist[1:3] = ["AI","Machine Learning"]
print(mylist)
mylist[1:1]= ["test","test"]
print(mylist)
mylist[1:3] = []
print(mylist)

for item in mylist:
    print(item)

for item in mylist:
    if item == "Django":
        print("Found Django!")

# Here i perform Copy of list
mylist_copy = mylist
print(mylist_copy)
mylist.append("SQL")
print(mylist) # This will show "SQL" because we appended it to mylist
print(mylist_copy) # This will also show "SQL" because mylist_copy is referencing the same list as mylist

# To create a true copy of the list, we can use the copy() method or slicing
mylist_copy2 = mylist.copy() # Using copy() method
mylist.append("NoSQL")
print(mylist) # This will show "NoSQL"
print(mylist_copy2) # This will not show "NoSQL" because mylist_copy2 is a separate copy of the list

mylist2 = ["Flask", "Django", "FastAPI"]
mylist3 = mylist + mylist2
print(mylist3)

union = []
for item in mylist3:
    if item not in union:
        union.append(item)

print(union)

squard_nums = []
for num in range(1,11):
    squard_nums.append(num**2)
print(squard_nums)