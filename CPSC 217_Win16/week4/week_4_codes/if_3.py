
marks = float(input("Enter a marks : "))

if (marks < 0) :
	print("Invalid marking......")
elif (marks > 100) :
	print("Invalid marking......")
elif (marks >= 90) :
	print("Grade: A")
elif (marks >= 80) :
	print("Grade: B")
elif (marks >= 70) :
	print("Grade: C")
elif (marks >= 60) :
	print("Grade: D")
else :
	print("Grade: F")
