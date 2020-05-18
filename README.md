MADE BY ALI RAZZAK DURING Bioinformatics MSc AT UNIVERSITY OF AUCKLAND
For "indexsplitaa.py" to be run in Python2.7

This script takes a list of amino acids (as defined in the script) and returns all the index values associated with those amino acids in reference to a .gro file.
Intended to be used with gromacs molecular dynamics pipeline.

Takes two inputs:
1) Name of file to output indexes to
2) Name of gromacs file to use as reference

For "formatxvgspaces.py" to be run in Python2.7

Simply takes an .xvg file (as typically produced by VMD or gromacs tools) and strips away headers and footers as well as reformats x axis so its step size is 1.

Takes three inputs:
1) .xvg file to edit
2) file to save to.
3) where to start counting x-ais from (initiate x)

For "breakingupcatpdb.py" to be run in Python2.7

Upon uploading a trajectory file (.dcd or .xtc) onto VMD the concatenated pdb files can be downloaded into a single file. This script reads that concatenated file and splits it into its constituent PDB frames.

The file takes three inputs, 1) the concatenated file, 2) the name format of the file it splits it into, each file is numbered at the end.
