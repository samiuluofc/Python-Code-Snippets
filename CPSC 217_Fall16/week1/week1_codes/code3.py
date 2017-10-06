# Write a program that will take Radius value from
# you/user, print the area and perimeter value of the
# circle.

r = input("Enter Radius value: ")

R = float(r);

area =  3.1416 * R * R
peri = 2 * 3.1416 * R

print("Area of the circle: %.2f.\nPerimeter of the circle %.2f." %(area, peri))
