# Write a program that will take three number from
# you/user, and show the average of these three
# number.

x = input("First number: ")
y = input("Second number: ")
z = input("Third number: ")

num1 = float(x);
num2 = float(y);
num3 = float(z);

avg = (num1 + num2 + num3)/3

print("The average of given three numbers is: ", avg)
