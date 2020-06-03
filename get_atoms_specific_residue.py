from string import digits
#requires python2.7

#get index of atom types in list can add more
aainterest=["CA","C","N"]

print (len(aainterest))

emptynumbers=[]
#where the atoms will be saved to
file=open('AAonlycarbonylbackbone.txt','w')
#where im writing the output to
for aminoacid in aainterest:
	allindex=""
	linecount=0
	#Reference file
	with open("KstRFromLigfirst.gro") as f:
		#name of file, probably something *first.gro
		for line in f:
			linecount=linecount+1
			if linecount>2:
				splitline=line.split()
				stringsplitline=splitline[0]
				stringsplitlinesection=stringsplitline.translate(None, digits)
				if splitline[1]==aminoacid:
					#only for this specific reisdue (alanine)
					if stringsplitlinesection=="ALA":
						#change residue if need be
						allindex=allindex+splitline[2]+" "
	splitindex=allindex.split()
	emptynumbers=emptynumbers+splitindex
emptynumbers.sort(key=int)

for chars in emptynumbers:
	file.write(chars+"\n")
	
