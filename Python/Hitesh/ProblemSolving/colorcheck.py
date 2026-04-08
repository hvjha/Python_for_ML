# Fruit = "Banana"

# color = input("Enter the color of the fruit: ").lower()
# if Fruit == "banana":
#     if color == "green":
#         print("The fruit is unripe.")
#     elif color == "yellow":
#         print("The fruit is ripe.")
#     else:
#         print("The fruit is overripe.")


# fruits = ["banana", "apple", "guava"]

# fruit = input("Enter fruit name: ").lower()
# color = input("Enter the color of the fruit: ").lower()

# if fruit in fruits:
#     if fruit == "banana":
#         if color == "green":
#             print("The fruit is unripe.")
#         elif color == "yellow":
#             print("The fruit is ripe.")
#         else:
#             print("The fruit is overripe.")
#     elif fruit == "apple":
#         if color == "red":
#             print("The fruit is ripe.")
#         elif color == "green":
#             print("The fruit is unripe.")
#         else:
#             print("The fruit is overripe.")
#     elif fruit == "guava":
#         if color == "green":
#             print("The fruit is unripe.")
#         elif color == "yellow":
#             print("The fruit is ripe.")
#         else:
#             print("The fruit is overripe.")
# else:
#     print("Fruit not found in list.")


fruit_color = {
    "banana": {
        "green": "The fruit is unripe.",
        "yellow": "The fruit is ripe.",
        "other": "The fruit is overripe."
    },
    "apple": {
        "red": "The fruit is ripe.",
        "green": "The fruit is unripe.",
        "other": "The fruit is overripe."
    },
    "guava": {
        "green": "The fruit is unripe.",
        "yellow": "The fruit is ripe.",
        "other": "The fruit is overripe."
    }
}

fruit = input("Enter fruit name: ").lower()
color = input("Enter the color of the fruit: ").lower()
if fruit in fruit_color:
    if color in fruit_color[fruit]:
        print(fruit_color[fruit][color])
    else:
        print(fruit_color[fruit]["other"])