pass1 = input("Enter Password (Maximum 10 letters, Minimum 6 letters):")

pass2 = input("Enter Same password again for authentication: ")

while pass1 != pass2:
    print("Password mismatch, try again.....")
    pass2 = input("Enter Same password again for authentication: ")


print("Successful Login")    
