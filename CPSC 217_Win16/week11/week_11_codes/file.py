#To read:
inf = open("input.txt", "r")
allText = inf.read() # read all text to a string
print(allText)
inf.seek(0,0)
line1 = inf.readline() # read one line at a time
print(line1, end = "")
print(len(line1))
line2 = inf.readline() # read one line at a time
print(line2, end = "")
print(len(line2))
inf.close()


#To write:
outf = open("output.txt", "w")
line2 = "wasiur\n"
outf.write(line2) # \n is not added by default
outf.write(line1) 
outf.close()
