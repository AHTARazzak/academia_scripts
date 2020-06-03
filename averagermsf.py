from matplotlib  import cm
import numpy as np
import sys

filename=str(sys.argv[1])

#range depends on # of windows
for i in range(1,51):
	diffcheck=0
	count=1
	residcount=1
	same=1
	samecount=1
	sametotal=0
	sameresidcounter=1
	file=open('sure.txt','w')
	#with open(filename+str(i)+'.xvg') as f:
	with open(filename+str(i)+'.xvg') as f:
		for line in f:
			if not "@" in line:
				if not "#" in line:
					splitline=line.split()
					newreference=int(splitline[0])
					if count<2:
						oldreference=int(splitline[0])
						file.write((str(count) + " " + str(splitline[1])+"\n"))
						count=count+1
					else:
						if (newreference-oldreference)==1:
							file.write(str(residcount)+" "+str(splitline[1])+"\n")
							oldreference=newreference
						elif (newreference-oldreference)>1:
							residcount=residcount+1
							file.write(str(residcount)+" "+str(splitline[1])+"\n")
							#file.write(str(splitline[1])+"\n")
							oldreference=int(splitline[0])
	f.close()
	file.close()
	with open("sure.txt") as c:
		filenew=open("proc"+filename+str(i)+".xvg",'w')
		for line in c:
			splitlinesure=line.split()
			if int(splitlinesure[0])==same:
				sametotal=sametotal+float(splitlinesure[1])
				samecount=samecount+1
			else:
				filenew.write(str(same)+" "+str(float(sametotal)/float(samecount-1))+"\n")
				same=same+1
				samecount=1
				sametotal=0
		filenew.write(str(same)+" "+str(float(sametotal)/float(samecount-1))+"\n")