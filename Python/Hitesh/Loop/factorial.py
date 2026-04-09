number = int(input("Enter the number: "))
factorial = 1

# for i in range(1,number+1):
#     factorial *= i
# print(f"The factorial of {number} is: {factorial}")

while number > 0:
    factorial *= number
    number -= 1
print(f"The factorial is: {factorial}")