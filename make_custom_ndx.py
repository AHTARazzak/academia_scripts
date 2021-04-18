# Requires Python3
import subprocess
import sys

filename = str(sys.argv[1])
startdx = str(sys.argv[2])
enddx = str(sys.argv[3])
newdx = str(sys.argv[4])

indexcombine=[]
with open(filename+'.ndx') as infile:
	copy = False
	for line in infile:
		if line.strip() == "[ " + startdx + " ]":
			copy = True
		elif line.strip() == "[ " + enddx + " ]":
			copy = False
		elif copy:
			splitentry = line.split()
			indexcombine = indexcombine + splitentry

indexstart = indexcombine[0]
count = 0
arraycount = 1
thisarray = []
for value in indexcombine:
	if int(indexcombine[count]) - int(indexcombine[count - 1]) > 1:
		thisarray.insert(count,"\n[ " + newdx + str(arraycount+1) + " ]\n")
		arraycount = arraycount + 1
	else:
		thisarray.append(value + " ")
	count = count + 1
	
thisarray.insert(0,"[ " + newdx + "1 ]\n")	
with open(filename+'.ndx', 'a') as outfile:
	for value in thisarray:	
		outfile.write(value)