
provinces = {"T":"Alberta", "V":"British Columbia", "R":"Manitoba", "E":"New Brunswick", "A":"Newfoundland", "B":"Nova Scotia", "X":"Nunavut or Northwest Territories", "K":"Ontario", "L":"Ontario", "M":"Ontario", "N":"Ontario", "P":"Ontario", "C":"Prince Edward Island", "G":"Quebec", "H":"Quebec", "J":"Quebec", "S":"Saskatchewan", "Y":"Yukon"}

postalcode = input("Enter a 6 character postal code(A1A1A1):")
first_letter_of_pc = postalcode[0]

print("This postal code resides in", provinces[first_letter_of_pc])
