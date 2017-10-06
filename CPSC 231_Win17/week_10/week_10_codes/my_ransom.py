import sys
import random
import filetest

def ransom(L):
	for line in L:
		newline = ''
		for ch in line:
			if ch.isalpha():
				if random.randint(0, 1) == 0:
					ch = ch.lower()
				else:
					ch = ch.upper()
			newline = newline + ch
		print(newline, end='')

def main():

        # Cheacking whether number of arguments are ok or not.
        if len(sys.argv) != 2:
                print('Usage: python3', sys.argv[0], 'filename')
                sys.exit()

        
        L = filetest.readlines(sys.argv[1])

        # Cheacking whether there is error during file read
        if L == None:
                print('Error with file', sys.argv[1])
                sys.exit()

        # If everything is ok, then invoke ransom function.
        ransom(L)


main()
