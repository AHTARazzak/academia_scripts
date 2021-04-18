# Requires Python3
from string import digits
import sys

# File to read
fileread = str(sys.argv[1])
# File outputing to
fileout = str(sys.argv[2])
# Start number of file
startnumber = float(sys.argv[3])
# Range end for filling
finalnum = int(sys.argv[4])
# What number to put into column two
fillwith = str(sys.argv[5])

count = startnumber

file = open(fileout,'w')

for x in range(0, finalnum):
	with open(fileread) as f:
		for line in f:
			linesplit = line.split()
			if float(linesplit[0]) == float(count):
				file.write(str(float(count)) + " " + linesplit[1] + "\n")
				count = count + 1
		else:
			file.write(str(float(count)) + " " + fillwith + "\n")
			count=count + 1
		f.close()