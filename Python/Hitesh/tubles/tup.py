tea_type = ("Masala Chai", "Green Tea", "Black Tea")
print(tea_type)

print(tea_type[0])
print(tea_type[1:3])    
print(tea_type[:2])
print(tea_type[:])
print(tea_type[1:3:2])

# tea_type[0] = "Herbal Tea" # This will raise an error because tuples are immutable  
# print(tea_type)

print(len(tea_type))

more_tea = ("Oolong Tea", "White Tea")
all_tea = tea_type + more_tea
print(all_tea)

for tea in all_tea:
    if tea == "Green Tea":
        print("Found Green Tea!")

more_tea = ("Oolong Tea", "White Tea","black Tea")
print(more_tea)
print(more_tea.count("black Tea"))
print(more_tea.index("Oolong Tea"))

(Masala_Chai, Green_Tea, Black_Tea)  = more_tea
print(Masala_Chai)
print(Green_Tea)

print(type(tea_type))

