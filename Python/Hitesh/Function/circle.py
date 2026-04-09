def circle(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return area, circumference
radius = float(input("Enter the radius of the circle: "))
area, circumference = circle(radius)
print(f"Area: {area}")
print(f"Circumference: {circumference}")