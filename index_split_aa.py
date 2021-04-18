# Requires Python3
from string import digits
import sys

# Residue of interest
aainterest = ["ALA"]
aalistnumbers = []
aalistnumbersnew = []
writeindextofile = str(sys.argv[1])
readgrofile = str(sys.argv[2])

file = open(writeindextofile,'w')
# Where im writing the output
for aminoacid in aainterest:
	allindex = ""
	with open(readgrofile) as f:
		# Read file something *first.gro
		for line in f:
			splitline = line.split()
			stringsplitline = splitline[0]
			stringsplitlinesection = stringsplitline.translate(None, digits)
			if stringsplitlinesection == aminoacid:
				allindex = allindex + splitline[2] + " "
				aalistnumbers = aalistnumbers + [splitline[0]]
splitallindex = allindex.split()
for chars in splitallindex:
	file.write(chars + "\n")
file.close()
for i in aalistnumbers:
	if i not in aalistnumbersnew:
		aalistnumbersnew.append(i)