def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
result = sum_all(1, 2, 3, 4, 5)
print(f"The sum of the numbers is: {result}")

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))
print(sum_all(10, 20, 30))
print(sum_all(5, 10, 15, 20))