import subprocess
import sys
import os
import math

#cav1 resid: 89 93 104 138 142 146
#cav1 ca: 1429,1486,1683,2193,2271,2332]
#cav2 resid: 72 104 107 108 135 138 139
#cav2 ca: 1153 1683 1737 1756 2140 2193 2213
#cav3 resid: 7 75 76 80 82 134 137 138
#cav3 ca: 88 1189 1208 1293 1317 2130 2174 2193
#cav4 resid: 25 28 29 65 68 69 72 107 111
#cav4 ca: 375 411 430 1057 1094 1153 1737 1792

#fileformat to read
pdbread=str(sys.argv[1])
#this atom (XE1,XE2,XE3,XE4) in our case
checkatomname=str(sys.argv[2])
#which file to start from (number)
startiterations=int(sys.argv[3])
#which file to end at (number)
numberiterations=int(sys.argv[4])
countone=0
counttwo=0
cavindex1=['88','1189','1208','1293','1317','2130','2174','2193']
cav1x=float(0)
cav1y=float(0)
cav1z=float(0)
cavindex2=['1153','1683','1737','1756','2140','2193','2213']
cav2x=float(0)
cav2y=float(0)
cav2z=float(0)
#cutoff angstrom
cutoff=int(sys.argv[5])
bump=float(50)
writeit1=open("pdblist1.txt","w+")
writeit2=open("pdblist2.txt","w+")
writevecdif1=open("writevecdif1.txt","w+")
writevecdif2=open("writevecdif2.txt","w+")
writevecdif1r=open("writevecdif1r.txt","w+")
writevecdif2r=open("writevecdif2r.txt","w+")
writevecdifr1r2a=open("writevecdifr1r2a.txt","w+")
writevecdifr1r2b=open("writevecdifr1r2b.txt","w+")
for i in range(startiterations,numberiterations+1):
	with open(pdbread+str(i)+".crd") as f:
		for line in f:
			splitline=line.split()
			if len(splitline)>3:
				if str(splitline[0]) in cavindex1:
					cav1x=cav1x+(float(splitline[4])+bump)
					cav1y=cav1y+(float(splitline[5])+bump)
					cav1z=cav1z+(float(splitline[6])+bump)
				if str(splitline[0]) in cavindex2:
					cav2x=cav2x+(float(splitline[4])+bump)
					cav2y=cav2y+(float(splitline[5])+bump)
					cav2z=cav2z+(float(splitline[6])+bump)
					#print splitline[5:8]
				if (splitline[2]==str(checkatomname)):
					vectorindex3=math.sqrt(((float(splitline[4])+bump)**2+(float(splitline[5])+bump)**2+(float(splitline[6])+bump)**2))
	cav1xavg=cav1x/float(len(cavindex1))
	cav1yavg=cav1y/float(len(cavindex1))
	cav1zavg=cav1z/float(len(cavindex1))
	cav2xavg=cav2x/float(len(cavindex2))
	cav2yavg=cav2y/float(len(cavindex2))
	cav2zavg=cav2z/float(len(cavindex2))
	vectorindex1=math.sqrt(((cav1xavg)**2+(cav1yavg)**2+(cav1zavg)**2))
	vectorindex2=math.sqrt(((cav2xavg)**2+(cav2yavg)**2+(cav2zavg)**2))
	#print cav1xavg-50
	#print cav1yavg-50
	#print cav1zavg-50
	#print cav2xavg-50
	#print cav2yavg-50
	#print cav2zavg-50
	cav1x=float(0)
	cav1y=float(0)
	cav1z=float(0)
	cav2x=float(0)
	cav2y=float(0)
	cav2z=float(0)
					
	difference1=math.sqrt(((vectorindex3)-(vectorindex1))**2)
	difference2=math.sqrt(((vectorindex3)-(vectorindex2))**2)
	#print difference1
	#print difference2
	if difference1<difference2:
		if difference1<cutoff:
			countone+=1
			writeit1.write(str(i)+" ")
			writevecdif1.write(str(i)+" "+str(difference1)+"\n")
			writevecdifr1r2a.write(str(difference1)+" "+str(difference2)+"\n")

	if difference2<difference1:
		if difference2<cutoff:
			counttwo+=1
			writeit2.write(str(i)+" ")
			writevecdif2.write(str(i)+" "+str(difference2)+"\n")
			writevecdifr1r2b.write(str(difference1)+" "+str(difference2)+"\n")


print checkatomname+" in pocket 3 "+str(countone)
print checkatomname+" in pocket 2 "+str(counttwo)
#print vectorindex1
#print vectorindex2
#print vectorindex3