#Create list
low_temps = [1.4, -1.8, 0.7, 0.9, 1.2, -2.2, -0.3]
names = ["Diana", "Bruce", "Clark"]
stuff = [1, "ICT", 3.14, "UofC"]
empty = []

#List access using index
print(stuff[0])

stuff[0] = "UofC"

print(stuff[0])
print(stuff)

#Loops and list
for ele in stuff:
    print(ele, end = ' ')

print()

for ind in range(0,len(stuff),1):
    print(stuff[ind], end = ' ')

print()

#List append, insert, remove and searching

num = [11,12,13,14,15,16,17,17]
num.append(18) # add 18 at the end of the list
print(num)

num.insert(4,50) # insert 50 at the index 4 of the list
print(num)

if 17 in num:
    print("Found")
else:
    print("Not Found")

print(num.index(17))

num.remove(17) # Remove an element
print(num)

print(num.pop(5)) # Remove the element at index 5
print(num.pop()) # Remove the last element
print(num)

# Sorting
num = [[6,5,2,1,7],[8,2,1,1,0,4,9,2]]
print(num[1].index(8))
#print(num)
#sort_num = sorted(num)
#print(sort_num)
#print(num)

#num.sort()
#print(num)









