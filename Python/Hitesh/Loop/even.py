even_Num = int(input("Enter the number: "))
sum = 0

for num in range(1,even_Num+1):
    if(num % 2==0):
        sum += num
print(f"Sum of even numbers from 1 to {even_Num} is: {sum}")