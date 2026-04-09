while True:
    number = int(input("Enter a Number: "))
    if number in range(1, 11):
        print(f"You entered valid Number: {number}")
        break
    else:
        print("Invalid Number. Please enter a number between 1 and 11.")