Mark = int(input("Enter your mark: "))

if Mark >100:
    print("Invalid mark. Mark cannot be greater than 100.")
    exit()

if Mark >=90:
    print("Grade A")
elif Mark >=80:
    print("Grade B")
elif Mark >=70:
    print("Grade C")
elif Mark >=60:
    print("Grade D")
else:
    print("Grade F")
