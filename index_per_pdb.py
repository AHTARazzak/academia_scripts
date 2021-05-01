import os
import re

pdb_series_name = input("Name of pdb series: ")
number_of_first_pdb = input("Number of first pdb in series: ")
number_of_last_pdb = input("Number of last pdb in series: ")
index_output_name = input("Name of index series: ")
group_names = list(input("Name of groups: "))

for i in range(int(number_of_first_pdb), int(number_of_last_pdb)):
	os.system("echo '8' | $GMX pdb2gmx -f " + pdb_series_name + str(i) + ".pdb -o tempgro.gro -water tip3p")
	all_indexes = list()
	final_string = ""
	with open('tempgro.gro', "r") as gro_file:
		this_group = list()
		begin_num = 0
		for line in gro_file.readlines()[2:-2]:
			if len(line) > 0:
				if int(re.findall("\d+", line.split()[0])[0]) >= begin_num:
					this_group.append(str(line.split()[2]))
					begin_num = int(re.findall("\d+", line.split()[0])[0])
				else:
					all_indexes.append(this_group)
					this_group = list()
					begin_num = int(re.findall("\d+", line.split()[0])[0])
					this_group.append(str(line.split()[2]))
	#print(all_indexes)
	for j in range(len(all_indexes)):
		final_string += "[ " + group_names[j] + " ]\n" + " ".join(all_indexes[j]) + "\n"
	#print(final_string)
	final_index = open(index_output_name + str(i) + ".ndx", "w")
	final_index.write(final_string)
	os.system("rm *#*")

