# Requires Python3
from string import digits
import sys

editfile = str(sys.argv[1])
savepoint = str(sys.argv[2])
xplot = int(sys.argv[3])

allindex = ""
file = open(savepoint,'w')
# Where im writing the file
with open(editfile) as f:
# What xvg stuff its reading
	for line in f:
		if "@" not in line:
			if "#" not in line:
				linesplit = line.split()
				if len(linesplit)>1: 
					allindex = str(xplot) + "   " + linesplit[1]
					xplot = xplot + 1
					file.write(allindex + "\n")
	
