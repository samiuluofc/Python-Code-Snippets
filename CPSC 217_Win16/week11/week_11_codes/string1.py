str1 = "SamiUL"
str2 = "university of calgary, calgary, alberta, canada"

print(str1)
print(str1[0])
print(str1[2:5])
print(str1[4:])
print(str1[:4])

print(len(str1))



print(str1.upper())
print(str1.lower())
print(str1[5].islower())
print(str1[5].isupper())
print(str1.isupper())

print(str1.swapcase())
print(str1.rjust(10))
print(str1.center(10))

print(str2.count(" "))
print(str2.count("c"))
print(str2.count("lg"))

print(str2.find(" "))
print(str2.find(" ",20))
print(str2.find(" ",25,40))
print(str2.rfind(" "))

print(str2.split(" "))
new_list = str2.split(",")

for sub in new_list:
    print(sub)













