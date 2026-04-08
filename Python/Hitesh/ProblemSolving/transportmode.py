distance = float(input("Enter the distance to be traveled (in km): "))
if distance < 0:
    print("Invalid distance. Distance cannot be negative.")
    exit()
if distance <3:
    transport_mode = "Walk"
elif distance < 15:
    transport_mode = "Bike"
else:
    transport_mode = "car"
print(f"Recommended mode of transport: {transport_mode}")