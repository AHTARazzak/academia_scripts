# Requires Python2.7
from string import digits
import sys
import subprocess
from math import *

# This can now be done internallty using gmx tools (gromacs)
linecount = 0
xplot = 1
# File with RMSF values
filename = str(sys.argv[1])
# New file with RMSF converted to B-factor
fileout = str(sys.argv[2])
file = open(fileout,'w')

with open(filename) as f:
	for line in f:
		if "@" not in line:
			if "#" not in line:
				linesplit = line.split()
				bfac = ((8*pi**2)/3) * (float(linesplit[1]) * 10)**2
				print(bfac)
				allindex = str(xplot) + "   " + str(bfac)
				xplot = xplot + 1
				file.write(allindex + "\n")
	
