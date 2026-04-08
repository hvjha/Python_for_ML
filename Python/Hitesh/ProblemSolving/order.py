# order_sizes = ["small", "medium", "large"]
# coffee_types = ["capuccino", "latte", "espresso"]

# order = input("Enter the size of your order (small, medium, large): ").lower()
# coffee = input("Enter the type of coffee you want (capuccino, latte, espresso): ").lower()
# extra_shot_input = input("Do you want an extra shot? (yes/no): ").lower()

# extra_shot = extra_shot_input == "yes"

# if order in order_sizes and coffee in coffee_types:
#     if extra_shot:
#         message = f"You ordered {order} {coffee} coffee with extra shot"
#     else:
#         message = f"You ordered {order} {coffee} coffee"
# else:
#     message = "Invalid order"

# print(message)


# order_sizes = ["small", "medium", "large"]
# coffee_types = ["capuccino", "latte", "espresso"]

# prices = {
#     "small": 100,
#     "medium": 150,
#     "large": 200
# }

# extra_shot_price = 30

# order = input("Enter the size (small, medium, large): ").lower()
# coffee = input("Enter coffee type (capuccino, latte, espresso): ").lower()
# extra_shot_input = input("Extra shot? (yes/no): ").lower()

# extra_shot = extra_shot_input == "yes"

# if order in order_sizes and coffee in coffee_types:
#     total_price = prices[order]  

#     message = f"You ordered a {order} {coffee} coffee"

#     if extra_shot:
#         total_price += extra_shot_price
#         message += " with an extra shot"

#     print(message)
#     print(f"Total price: ₹{total_price}")
# else:
#     print("Invalid order")

order_sizes = ["small", "medium", "large"]
coffee_types = ["capuccino", "latte", "espresso"]

size_price = {
    "small": 100,
    "medium": 150,
    "large": 200
}

cofee_prices = {
    "capuccino": 20,
    "latte": 30,
    "espresso": 40
}

extra_shot_price = 30

order = input("Enter the size (small, medium, large): ").lower()
coffee = input("Enter coffee type (capuccino, latte, espresso): ").lower()
quantity = int(input("Enter quantity: "))
extra_shot_input = input("Extra shot? (yes/no): ").lower()

extra_shot = extra_shot_input == "yes"

if order in order_sizes and coffee in coffee_types:
    total_price = (size_price[order] + cofee_prices[coffee]) * quantity

    message = f"You ordered {quantity} {order} {coffee} coffee"

    if extra_shot:
        total_price += extra_shot_price * quantity
        message += " with extra shot"

    print(message)
    print(f"Price per cup: ₹{size_price[order] + cofee_prices[coffee] + (extra_shot_price if extra_shot else 0)}")
    print(f"Total price: ₹{total_price}")