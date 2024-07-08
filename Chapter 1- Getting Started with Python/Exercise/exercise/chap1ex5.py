import math

def compute_area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle with radius {radius} is: {area}")

compute_area_of_circle()
