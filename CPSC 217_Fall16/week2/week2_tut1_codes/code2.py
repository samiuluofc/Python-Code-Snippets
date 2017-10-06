# Write a program that asks the user for the number of males
# and the number of females registered in a class.
# The program should display the percentage of males and females in the class.

#Taking inputs
n_males = float(input("Enter number of males : "))
n_females = float(input("Enter number of females : "))


# Calculating percentage
total_stu = n_males + n_females
per_males = (n_males / total_stu) * 100
per_females = 100 - per_males


#Showing necessary outputs
print("Percentage of males : %.2f" % per_males,"%")
print("Percentage of females : %.2f" % per_females,"%")



