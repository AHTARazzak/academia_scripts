import subprocess
import sys
import os
import math

# Script finds index of atom types in PDB and selects them from RMSF file
# Ensure that the RMSF file contains all atoms
# Best used with GROMACS RMSF tool

readfile1 = str(sys.argv[1])
# PDB file to get atoms from
readfile2 = str(sys.argv[2])
# RMSF file to where all atoms stored
outfile = str(sys.argv[3])
# edit rmsf file

aainterest = ["CA"]
# Carbonyl backbone CA, can increase selection for other atoms
print(len(aainterest))

emptynumbers = []
file = open(readfile1,'r')
# Where im writing the output to
for aminoacid in aainterest:
	allindex = ""
	linecount = 0
	with open(readfile1) as f:
		# Name of file, probably something *first.gro
		for line in f:
			linecount = linecount + 1
			if linecount > 2:
				splitline = line.split()
				if splitline[2] == aminoacid:
					allindex = allindex+splitline[1] + " "
	splitindex = allindex.split()
	emptynumbers = emptynumbers + splitindex

emptynumbers.sort(key = int)

file2 = open(readfile2,"r")
fileout = open(outfile,"w")
for line in file2:
	cutline = line.split()
	print line
	if "#" not in line:
		if "@" not in line:
			if int(cutline[0]) in emptynumbers:
				fileout.write(line + " \n")