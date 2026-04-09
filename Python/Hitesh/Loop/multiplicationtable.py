number = int(input("Enter the number: "))

print(f"Multiplication table of {number}:")
for i in range(1, 11):
    result = number * i
    if(i ==5):
        continue
    print(f"{number} x {i} = {result}")

