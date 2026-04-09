# This code identifies unique items and duplicates from a list of items.
items = ["apple", "banana", "cherry", "apple", "date", "banana"]

unique_items = set()
duplicates = set()

for item in items:
    if item in unique_items:
       duplicates.add(item)
    else:
        unique_items.add(item)

print("duplicates:", duplicates)
print("unique items:", unique_items)


#Find first duplicate item in a list
items = ["apple", "banana", "cherry", "apple", "date", "banana"]

seen = set()
duplicate = set()

for item in items:
    if item in seen:
        duplicate.add(item)
        break
    else:
        seen.add(item)

print("First duplicate item:", duplicate)
