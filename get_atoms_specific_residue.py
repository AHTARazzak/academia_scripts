# Requires Python3
from string import digits

# Get index of atom types in list can add more
aainterest = ["CA","C","N"]

emptynumbers = []
# Where the atoms will be saved to
file = open('AAonlycarbonylbackbone.txt','w')
# Where im writing the output to
for aminoacid in aainterest:
	allindex = ""
	linecount = 0
	# Reference file
	with open("KstRFromLigfirst.gro") as f:
		# Mame of file, probably something *first.gro
		for line in f:
			linecount = linecount+1
			if linecount>2:
				splitline = line.split()
				stringsplitline = splitline[0]
				stringsplitlinesection = stringsplitline.translate(None, digits)
				if splitline[1] == aminoacid:
					# Only for this specific reisdue (alanine)
					if stringsplitlinesection == "ALA":
						# Change residue if need be
						allindex = allindex+splitline[2] + " "
	splitindex = allindex.split()
	emptynumbers = emptynumbers + splitindex
emptynumbers.sort(key = int)

for chars in emptynumbers:
	file.write(chars + "\n")