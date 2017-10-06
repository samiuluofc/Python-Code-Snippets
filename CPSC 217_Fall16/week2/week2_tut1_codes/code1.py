# Write a program that calculates the total amount of a meal purchased
# at a restaurant. The program should ask the user to enter the charge
# for the food, and then calculate the amount of 18 percent tip and 7 percent
# sales tax. Display each of these amounts and the total.
# Use comments and decent formatting for input and outputs.

# Taking inputs
food_cost = input("Enter food cost (in $) : ")
food_cost = float(food_cost)

# Total cost calculation

sales_tax_per = 0.07
tips_per = 0.18

sales_tax = food_cost * sales_tax_per
tips = food_cost * tips_per
total_cost = food_cost + sales_tax + tips

# Showing necessary outputs
print("Total Cost: %.2f" % total_cost,"$")
print("Salex Tax: %.2f" % sales_tax,"$")
print("Tips Amount: %.2f" % tips,"$")
