mybook = {"title":"Introduction to python", "author":"Hitesh Choudhary", "year":2020}
print(mybook)
print(mybook["title"])  
print(mybook["author"])
print(mybook["year"])

mybook["publisher"] = "Code with chai"
print(mybook)
print(mybook["publisher"])
print(len(mybook))

for key in mybook:
    print(key)

for value in mybook.values():
    print(value)

for key in mybook:
    print(mybook[key])

for key, value in mybook.items():
    print(f"{key}: {value}")

mybook["year"] = 2024
print(mybook)

for book in mybook:
    if book == "year":
        print("Found year!", mybook[book])

mybook.pop("publisher")
print(mybook)

mybook.popitem() # Remove the last inserted item
print(mybook)

del mybook["author"]
print(mybook)

mybook_copy = mybook.copy()
print(mybook_copy)

library = {"book1": {"title": "Introduction to Python", "author": "Hitesh Choudhary", "year": 2020},
           "book2": {"title": "Advanced Python", "author": "Hitesh Choudhary", "year": 2021},
           "book3": {"title": "Python for Data Science", "author": "Hitesh Choudhary", "year": 2022}}
print(library)

print(library["book1"])
print(library["book1"]["title"])
print(library["book2"]["author"])   
print(library["book3"]["year"])

for book_key, book_info in library.items():
    print(f"{book_key}:")
    for key, value in book_info.items():
        print(f"  {key}: {value}")


squaare_dict = {}
for i in range(1, 11):
    squaare_dict[i] = i ** 2

print(squaare_dict)

cube_dict = {i : i** 3 for i in range (1,11)}
print(cube_dict)

keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]

mydict = {key: value for key, value in zip(keys, values)}
print(mydict)

my_dict = dict(zip(keys, values))
print(my_dict)




