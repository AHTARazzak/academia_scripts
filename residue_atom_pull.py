import subprocess
import sys
import os
import math

#This script takes the amino acid side chain atoms (or those not listed in aainterest) for each residue of interest in list residueinterest and writes them into their own file

#can add other atoms to exlude
aainterest=["CA","C","N","O","HN","HA"]
#residues wanted to target
residueinterest=["71","72","73","75","76","89","93","99","101","104","107","108","111","135","138","142","146",]
#pdb file being read
pdbread=str(sys.argv[1])
#identifier of molecule
molid="MB"
emptynumbers=[]
#collection of atoms selected into this file
file=open('proteinsidechain.txt','w')
thestring=""
with open(pdbread+".pdb") as f:
	for line in f:
		splitline=line.split()
		if len(splitline)>5:
			if splitline[2] not in aainterest:
				if splitline[4] in residueinterest:
					if splitline[10]==molid:
						thestring=thestring+splitline[1]+" "

file.write(thestring)

	
