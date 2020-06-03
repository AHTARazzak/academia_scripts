ALI RAZZAK SCRIPTS MADE DURING BIOINFORMATICIAN MSC @ UNIVERSITY OF AUCKLAND

"breaking_up_concat_pdb.py" run on Python 2.7
Takes series of concatenated PDB files (as produced from trajecory file saved from VMD) and splits them up into a series of PDB files.

takes two arguments:
1. Name of PDB file to be split (without ".pdb" extension).
2. Name of PDBf files to be produced (without ".pdb" extension).

"format_xvg_spaces.py" run on Python 2.7
Takes a .xvg file and removes all header and formating detail leaving only data, then reformats x-axis axis in steps of 1 start from where designated to wherever designated

Takes three arguments:
1. File to edited name.
2. File output name.
3. Which number to start x-series from.

"index_split_aa.py" run on Python 2.7
Takes out index number for specific amino acids (ideally used within Gromacs pipeline)

Takes two arguments:
1. Where to write index numbers.
2. Which .gro file to use as reference

"select_RMSF_atomtypes.py" run on Python 2.7
Edits produced full RMSF file for select atom types (ideally used within Gromacs pipeline)

Takes three arguments:
1. Reference PDB file.
2. Full RMSF file (ideally produced using gromacs RMSF tool http://manual.gromacs.org/current/onlinehelp/gmx-rmsf.html).
3. Edited RMSF file output name.
