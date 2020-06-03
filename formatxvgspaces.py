from string import digits
#requires python2.7
import sys


#this script reads a xvg file, removes all the gunk from the top and reformats the x axis into 1 step sizes starting from whereever
editfile=str(sys.argv[1])
savepoint=str(sys.argv[2])
xplot=int(sys.argv[3])

allindex=""
file=open(savepoint,'w')
#where im writing the file
with open(editfile) as f:
#what xvg stuff its reading
	for line in f:
		if "@" not in line:
			if "#" not in line:
				linesplit=line.split()
				if len(linesplit)>1: 
					allindex=str(xplot)+"   "+linesplit[1]
					xplot=xplot+1
					file.write(allindex+"\n")
	
