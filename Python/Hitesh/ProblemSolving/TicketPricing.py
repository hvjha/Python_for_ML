age = int(input("Enter your age: "))
day = input("Enter the day of the week: ").lower()

price = 12 if age >= 18 else 8
if day == "wednesday":
    price -= 2

print(f"Base price: ${price}")
