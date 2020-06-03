from string import digits

#file with higher values to subtract from
filehigh="KstRDNALonggyrateall1"
#file with lower values subtract
filelow="KstRDNALonggyrateLBDboth1"
filehighread=filehigh+".xvg"
filelowread=filelow+".xvg"
counttrack=1
#dummyfile with columns before subtraction
filenew=filehigh+"lamediff.xvg"
file=open(filenew,'w')
allindex=""
aindex=[]
counta=0
with open(filehighread) as f:
	with open(filelowread) as l:
		for line in f:
			if "@" not in line:
				if "#" not in line:
					linesplit=line.split()
					if len(linesplit)>1: 
						aindex.append(str(linesplit[1]))
		for line in l:
			if "@" not in line:
				if "#" not in line:
					linesplit=line.split()
					if len(linesplit)>1: 
						allindex=allindex+aindex[counta]+"   "+str(linesplit[1])+"\n"
						counta=counta+1
	file.write(allindex)

file.close()
linecount=0
differencegyrate=0
finalindex=""
#finalfinaltowriteto
filenewdif="KstRDNALonggyrateDBD.xvg"
file=open(filenewdif,'w')
with open(filenew) as a:
	for line in a:
		finalsplit=line.split()
		if len(finalsplit)>1:
			differencegyrate=float(finalsplit[0])-float(finalsplit[1])
			finalindex=finalindex+str(linecount)+"    "+str(differencegyrate)+"\n"
			linecount=linecount+1
	file.write(finalindex)
