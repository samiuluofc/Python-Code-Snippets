#To read:
inf = open("input.in", "r")
allText = inf.read() # read all text to a string
print(allText)


inf.seek(0) # take the pointer at the begining of the text again
line1 = inf.readline() # read one line at a time
print(line1, end = "")
print(len(line1))

line2 = inf.readline() # read one line at a time
print(line2, end = "")
print(len(line2))
inf.close() # closing a file


#To write:
outf = open("output.out", "w")
line1 = "A\nB\nC\n"
outf.write(line1) # \n is not added by default
outf.write("\n\nUofC") 
outf.close()
