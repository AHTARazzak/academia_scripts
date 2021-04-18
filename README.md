ALI RAZZAK SCRIPTS MADE DURING BIOINFORMATICIAN MSC @ UNIVERSITY OF AUCKLAND

"averagermsf.py" runs in Python2.7
Takes a file named in series as declared on command line input and calculates the average rmsf across the series of files. The RMSF .xvg files were produced using GROMACS. Intended to be used in the GROMACS command line.

Takes 1 argument:
1. Format of .xvg file series

"breaking_up_concat_pdb.py" run on Python2.7
Takes series of concatenated PDB files (as produced from trajectory file saved from VMD) and splits them up into a series of PDB files.

Takes 2 arguments:
1. Name of PDB file to be split (without ".pdb" extension).
2. Name of PDBf files to be produced (without ".pdb" extension).

"format_xvg_spaces.py" run on Python2.7
Takes a .xvg file and removes all header and formating detail leaving only data, then reformats x-axis axis in steps of 1 start from where designated to wherever designated

Takes 3 arguments:
1. File to edited name.
2. File output name.
3. Which number to start x-series from.

"index_split_aa.py" run on Python2.7
Takes out index number for specific amino acids (ideally used within Gromacs pipeline)

Takes 2 arguments:
1. Where to write index numbers.
2. Which .gro file to use as reference

"select_RMSF_atomtypes.py" run on Python2.7
Edits produced full RMSF file for select atom types (ideally used within Gromacs pipeline)

Takes 3 arguments:
1. Reference PDB file.
2. Full RMSF file (ideally produced using gromacs RMSF tool http://manual.gromacs.org/current/onlinehelp/gmx-rmsf.html).
3. Edited RMSF file output name.

Takes 5 arguments:
1. File to read.
2. File to output to.
3. Where to start the x-series from (better leave as "1").
4. where to end the x-series (better leave as "1").
5. What to fill into the y column.

"get_atoms_specific_residue.py" run on Python2.7
This reads a pdb file and returns a file with the index of specific atoms (as listed in aaindex) for specific residues (as identified on line 27).

Takes 0 arguments:
Important to format output file line 11, and reference file line 17.

"get_select_protein_atoms_index.py" run on Python2.7
Similar to "get_atoms_specific_residue.py" but not for a specific residue

Takes 0 arguments:
Important to format output file line 11, and reference file line 17.

"subtract_columns.py" run on Python2.7
Subtracts columns within two files from one another and returns file with subtracted values.

Takes 0 arguments:
Important to format output file as described in comments at lines 4, 6, and 37.

"rmsf_to_bfactor.py" run on Python2.7
Converts theoretical RMSF to theoretical bfactor to be used in gromacs pipeline although now available within GMX tools

Takes 2 arguments:
1. File with RMSF values
2. File to output B-factor values to.

"remove_column_one.py" run on Python2.7
Removes a column from a file.

Takes 2 arguments:
1. File with column to be removed.
2. File to output new data without column.

"protein_split_backbone_sidechain.py" run on Python3
Script runs through all residues in protein and splits into sidechain and backbone for each residue.

Takes 3 arguments:
1. Name of PDB desired to be  split.
2. Name of output files.
3. Which residue to begin splitting from.

"residue_atom_pull.py" run on Python3
This script takes all the atoms not in selection for each residue and outputs them to a file

Takes 1 arguments (but read file to modulate variable):
1. PDB file to read.

"early_poor_tracking_script_MB.py" run on Python3
This script was an early attempt at me making a cavity centre of mass (as defined by residues lining residue) tracking script.
It takes an atom and determines which of either pocket or pocket 2 it is in.
Intended for use with charmm after splitting trajectory into series of coordinate files (.cor or .crd)

Takes 3 arguments (but read file to modulate variable):
1. CRD files to read (series).
2. Atom being tracked (resname).
3. Which file to stop tracking at.
 
 ALI RAZZAK SCRIPT MADE DURING PHYSICAL CHEMISTRY PhD @ UNIVERSITY OF BASEL

For "combine_column_1s.py" to be run in Python2.7
Takes the first row of two files [x] and [y] and combines them into a single file with two rows [x y]. Particularly useful in preparation for the "make_ramachandran.py" script.

File takes 3 inputs:
1) File one containing a column.
2) File two containing columns.
3) File three combinations of column 1 from both files.

For "make_ramachandran.py" to be run in Python2.7
Takes a sequentially ordered list of dihedral angles so in column 1 x axis sequence and column 2 the dihedral angle. Produces 3D histogram of ramachandran plot and outputs onto customisable GUI.

File takes 2 inputs:
1) Fle containing time series of dihedral angles.
2) Number of bins in raster.

For "generic_make_3d_histogram.py" to be run in Python3
(Much more efficient 3d histogram)
takes 1 input:
1) Fle containing time series of dihedral angles.

For "calculate_cavity_cutoff_SURFNET.py" to be run in Python3

This cavity calculation script requires:
1) a working local compilation of CHARMM all atom simulation engine - see line 157 to make changes in executable.
2) a working local (in directory) installation of SURFNET (https://omictools.com/surfnet-tool)
Works best in tandem with https://github.com/ternlef11/Break_concat_pdb.git to break up concatenated pdb files and name files sequentially.
The specifications of the protein for surfnet should be modified for at line 42, the parameters about lines 63 to 67 can also be tinkered with depending on cae.
The charmm specifications should be adapted to circumstance (lines 168-201)
perhaps the charmm executable also might need specification depending on user version (line 210)

The scripts takes 5 inputs:
1) number of pdb files to iterate through
2) the bump number (incase of negative atom coordinates)
3) Cutoff for cavity selection
4) Upper volume cutoff
5) Name of output cavity file name

For "trackingscriptcrdcharmcomimp.py" to be run in Python3

This tracking script requires a working local compilation of CHARMM all atom simulation engine - see line 157 to make changes in executable.
This file tracks an atom within myoglobin and assigns it into 11 different possible allocations as defined by literature. It writes the atom assignment into 1 of the 11 allocations for every pdb file.
The system use and cavity allocation can be modulated, see line 66 onwards.

The assignments are:

1) Cavity 1
2) Cavity 2
3) Cavity 3
4) Cavity 4
5) Between cavity 2 and 1
6) Between cavity 2 and 3
7) Between cavity 2 and 4
8) Between cavity 1 and 3
9) Distal pocket
10) Outside proint
11) Between cavity 4 and distal pocket

The scripts takes 6 inputs:
1) the pdb name format (it assumes serial numbers at end, perhaps use following: https://github.com/ternlef11/Break_concat_pdb.git
2) Atom name to be tracked
3) Which pdb to start the track from (int)
4) Number of frames (from to track from starting) (int)
5) Cutoff for cavity assignments
6) System number (consider removing and change where applicable in script for your circumstance)

For "convert_dihed_energy.py" to be run in Python3

This script reads a sequence of PDB files and calculates the dihedral energy Hamiltonian term of each amino acid residue.

The scripts takes 2 inputs:
1) The name of the file naming pattern for each PDB structure.
2) The name of the file to output to.

For "dihedral_angle_avg_std.py" to be run in Python2.7

This file reads multiple .xvg files and returns the average and dihedral angle across all .xvg files

The scripts takes 2 inputs:
1) The name of the .xvg file naming pattern for each file containing dihedral angles structure.
2) The name of the file to output to.

For "charmm_hbond_ana_hard.py" to be run in Python3

This script runs charmm for hbond analysis for each residue.
Intended for use with charmm pipeline.
Only parsable for someone with charmm expertise.

The script takes 1 input:
1) File format to be read

For "charmm_hbond_ana_specific.py" to be run in Python3

This script runs charmm for hbond analysis for specific residues as selected in aa residue (line 12).
Intended for use with charmm pipeline.
Only parsable for someone with charmm expertise.

The script takes 1 input:
1) File format to be read

For "count_hbond_for_molecule_logfile_charmm.py" to be run in Python3

This script reads a charmm log file following Hbond analysis.
It then counts the number of Hbond for a given residue and molecule ID (line 17).
Intended for usage in CHARMM pipeline.

The script takes 1 input:
1) Name of .log file to search for hbonds.

For "file_avg_std_standarderror.py" to be run in Python2.7

READS THE XVG FILE
need to put script file in same directory as the avg
This file returns the mean, standard deviation, and standard error for data from determined point to the next (as specific line 19 and 21)
Output in terminal

Important to read file notes (details in script)

For "file_avg_std_standarderror_section.py" to be run in Python2.7

READS THE XVG FILE
need to put script file in same directory as the avg
This file returns the mean, standard deviation, and standard error for entire file per section for series of files.
section sizes dtermined line 25 and 27 (250 right now but can be changed)
Output in terminal and to file (see line 62)

Important to read file notes (details in script)

The script takes 1 input:
1) File format of series of files.

For "pull_lines_into_file.py" to be run in Python3

File pulls lines (as specified in aalist) into seperate files (see line 19).
Intended to be used with series of files and structural bioinformatic pipeline.

The script takes 1 input:
1) File format of series of files.

For "pvalue_consider_null.py" to be run in Python3

This file finds the p-value of data and determines whether to reject or accept null hypothesis.
Can modualte significance on line 24.

The script takes 1 input:
1) Name of file to process.

For "ss_dump_analysis.py" to be run in Python3

This file reads the secondary structure association for each residue and prints it out into a time series format (see line 20).
Intended to be used in groamcs pipeline. Need output from gmx ss_dump http://manual.gromacs.org/archive/5.0.5/programs/gmx-do_dssp.html.
Need -dump command output to be read.

Read notes in script file!

The script takes 2 input:
1) Reads ss dump output.
2) Saves to this file.

For "dccm_analysis_prep_file.py" to be run in Python3

This file gets the ABSOLUTE difference in DCCM between two files

The script takes 3 input:
1) DCCM File one contents.
2) DCCM File two contents.
3) File with outputted difference for each atom pair.

For "swap_columns_1_2.py" to be run in Python3

This file swaps columns 1 and 2 within a file.

The script takes 2 input:
1) Name of file with columns wanting to swap.
2) Name of file outputting to.

For "upper_and_lower_iqr.py" to be run in Python3

This script finds the upper and lower quartiles of data.
Does it for second column and must only contain data values.

The script takes 2 input:
1) Name of file to find quartiles for.