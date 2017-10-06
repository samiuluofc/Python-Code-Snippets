#To read:
inf = open("input.txt", "r")

line = inf.read() # read one line at a time
plist = line.split("\n\n")
print(plist)


inf.close()


#To write:
outf = open("output.txt", "w")
outf.write("Hello CPSC 217") # \n is not added by default
outf.write("Hello CPSC 217") # \n is not added by default

outf.close()
