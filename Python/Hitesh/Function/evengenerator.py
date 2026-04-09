def even_generator(n):
    for i in range(2,n+1):
        if i % 2 ==0:
            yield i
n = int(input("Enter a number: "))
even_numbers = even_generator(n)
print(f"Even numbers up to {n}:")
for num in even_numbers:
    print(num)
