# Requires Python3
import subprocess
import sys

# NEED TO HAVE FILE bashghecomvolume.sh in same directory
# Can edit the bash file for filename, outputname, and number of iterations
# Outputfile name from this script should match inputfile name of the bash script

# Argument 1: name of concatenated file to be split
# Argument 2: format of output file for each split
pdbtobesplit = str(sys.argv[1])
writename = str(sys.argv[2])

input = open(pdbtobesplit+'.pdb', 'r').read().split('END')
count = 0
for entry in input:
	count = count+1
	with open(writename+str(count) + '.pdb','w') as f:
		f.write(str(entry))
