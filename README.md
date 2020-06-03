ALI RAZZAK SCRIPTS MADE DURING BIOINFORMATICIAN MSC @ UNIVERSITY OF AUCKLAND

"breaking_up_concat_pdb.py" run on Python 2.7
Takes series of concatenated PDB files (as produced from trajecory file saved from VMD) and splits them up into a series of PDB files.

takes 2 arguments:
1. Name of PDB file to be split (without ".pdb" extension).
2. Name of PDBf files to be produced (without ".pdb" extension).

"format_xvg_spaces.py" run on Python 2.7
Takes a .xvg file and removes all header and formating detail leaving only data, then reformats x-axis axis in steps of 1 start from where designated to wherever designated

Takes 3 arguments:
1. File to edited name.
2. File output name.
3. Which number to start x-series from.

"index_split_aa.py" run on Python 2.7
Takes out index number for specific amino acids (ideally used within Gromacs pipeline)

Takes 2 arguments:
1. Where to write index numbers.
2. Which .gro file to use as reference

"select_RMSF_atomtypes.py" run on Python 2.7
Edits produced full RMSF file for select atom types (ideally used within Gromacs pipeline)

Takes 3 arguments:
1. Reference PDB file.
2. Full RMSF file (ideally produced using gromacs RMSF tool http://manual.gromacs.org/current/onlinehelp/gmx-rmsf.html).
3. Edited RMSF file output name.


peter.hauser@unibas.ch

Takes 5 arguments:
1. File to read.
2. File to output to.
3. Where to start the x-series from (better leave as "1").
4. where to end the x-series (better leave as "1").
5. What to fill into the the y column.

"residue_atom_pull.py" run on Python 3
This script takes all the atoms not in selection for each residue and outputs them to a file

Takes 1 arguments (but read file to modulate variable):
1. PDB file to read.

"early_poor_tracking_script_MB.py" run on Python 3
This script was an early attempt at me making a cavity centre of mass (as defined by residues lining residue) tracking script.
It takes an atom and determines which of either pocket or pocke 2 it is in.
Intended for use with charmm after splitting trajectory into series of coordinate files (.cor or .crd)

Takes 3 arguments (but read file to modulate variable):
1. CRD files to read (series).
2. Atom being tracked (resname).
3. Which file to stop tracking at.
  
