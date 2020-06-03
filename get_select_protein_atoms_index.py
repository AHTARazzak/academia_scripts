aainterest=["CA","C","N"]
#carbonyl backbone CA C N
print (len(aainterest))

emptynumbers=[]
file=open('onlycarbonylbackbone.txt','w')
#where im writing the output to
for aminoacid in aainterest:
	allindex=""
	linecount=0
	with open("KstRFromLigfirst.gro") as f:
		#name of file, probably something *first.gro
		for line in f:
			linecount=linecount+1
			if linecount>2:
				splitline=line.split()
				if splitline[1]==aminoacid:
					allindex=allindex+splitline[2]+" "
	splitindex=allindex.split()
	emptynumbers=emptynumbers+splitindex
emptynumbers.sort(key=int)

for chars in emptynumbers:
	file.write(chars+"\n")
	
