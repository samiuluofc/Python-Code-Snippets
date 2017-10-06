# This program takes pressure in kilopascals as input,
# then converts it to atmospheres, pounds per square inch,
# and millimetres of mercury

# Conversion factors
# Note: these are constants with ALL_CAPS
KPA_TO_ATM = 101.325
ATM_TO_MMHG = 760
ATM_TO_PSI = 14.6959

# Read pressure from the user
kPa = float(input("Enter a value in kilopascals: "))

# Conversion
atm = kPa / KPA_TO_ATM  
mmHg = atm * ATM_TO_MMHG
psi = atm * ATM_TO_PSI

# Display the results
print(kPa, "kilopascals is equal to", psi, "pounds per square inch.")
print(kPa, "kilopascals is equal to", atm, "atmospheres.")
print(kPa, "kilopascals is equal to", mmHg, "mmHg.")
