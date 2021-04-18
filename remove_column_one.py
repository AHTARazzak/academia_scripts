# Requires Python2.7
import subprocess
import sys
import decimal

# Remove column 1 from this file
filename = str(sys.argv[1])
# File without column one
fileout = str(sys.argv[2])

allwords = ""
with open(filename) as infile:
	for line in infile:
		linesplit = line.split()
		allwords = allwords + str(linesplit[1]) + " " + str(linesplit[2]) + "\n"

writefile = open(fileout,"w")
writefile.write(allwords)
