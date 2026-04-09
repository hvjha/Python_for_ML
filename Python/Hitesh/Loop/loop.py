# numbers = [1,-2,3,-4,5,6,-7,-8,9,10,12,45,67,-99,-23,34,56,-78,-90]
# count = 0
# for num in numbers:
#     if num <0:
#         continue
#     else:
#         count +=1
# print(f"count of Positive Numbers : {count}")

numbers = [1,-2,3,-4,5,6,-7,-8,9,10,12,45,67,-99,-23,34,56,-78,-90]

Possum = 0
Negsum = 0

for num in numbers:
    if num < 0:
        Negsum += num
    else:
        Possum += num

print(f"Sum of Positive Numbers : {Possum}")
print(f"Sum of Negative Numbers : {Negsum}")



