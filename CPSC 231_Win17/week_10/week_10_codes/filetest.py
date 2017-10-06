import sys

# Returns a list of lines that the text file specified by the filename
# contains, or None if there was some problem.

def readlines(filename):
	try:
		f = open(filename, 'r')
		rv = f.readlines()
		f.close()
	except IOError:
		rv = None
	return rv

if __name__ == '__main__':
	for filename in sys.argv[1:]:
		print(readlines(filename))
