import sys
import subprocess

#This script highlights all possible backbone atoms and divides residues in protein into abckbone and sidechain groups via index

atominterest=["H1 ", "H2 ", "H3 ", "HA ","O ", "OT1 ", "OT2 ", "HN ", "HA ", "CA ","C ","N "]

#Name of structure to be split
filename=str(sys.argv[1])
#where files will be output to
fileout=str(sys.argv[2])
#first residue number
initialnumber=int(sys.argv[3])
count=0
writeoutbb=""
writeoutsc=""
with open(filename) as f:
	for line in f:
		splitline=line.split()
		if (splitline[0]=="ATOM"):
			if initialnumber == int(splitline[5]):	
				if ((splitline[2])+" ") in atominterest:
					writeoutbb = writeoutbb + line
					filetowrite=open(str(fileout)+str(splitline[3])+str(splitline[5])+"_backbone.pdb", 'w')
					filetowrite.write(writeoutbb)
					print line
				elif ((splitline[2])+" ") not in atominterest:
					writeoutsc = writeoutsc + line
					filetowrite=open(str(fileout)+str(splitline[3])+str(splitline[5])+"_sidechains.pdb", 'w')
					filetowrite.write(writeoutsc)
					print line
			else:
				writeoutsc=""
				writeoutbb=line
				initialnumber=initialnumber+1
		
