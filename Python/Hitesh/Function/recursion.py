def fact(n):
    if n ==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
    
number = int(input("Enter a number to find its factorial: "))
result = fact(number)
print(f"The factorial of {number} is: {result}")    