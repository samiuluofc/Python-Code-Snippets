num = []

ch = input("Enter number (between 0 to 100): ")
while(ch != ""):
    num.append(float(ch))
    ch = input("Enter number (between 0 to 100): ")


print(num)

max_ele = 0
for ele in num:
    if ele > max_ele:
        max_ele = ele

print(max_ele)
        
