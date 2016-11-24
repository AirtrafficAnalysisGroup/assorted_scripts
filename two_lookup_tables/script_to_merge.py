#script that merges two csvs together!

import csv
from collections import defaultdict

#builds dictionary of list of tuples (WHOAAAAAAAAAAAA)
def fill_dict(csv_reader):
	out_dict = defaultdict(list)
	for row in csv_reader:
		key = row[1]
		out_dict[key].append((row[2],row[0]))
	return out_dict

def compare_states(st1, st2):
	return (st1 == st2) or (st1 in st2) or (st2 in st1)

with open('bls_lookup_sm.area.csv', 'r') as ec_table, open('bts_filtered_3_col.csv', 'r') as fl_table, open('merged_lookup.csv', 'w+') as outfile:
	ec_reader = csv.reader(ec_table)
	fl_reader = csv.reader(fl_table, delimiter=';')
	ec_dict = fill_dict(ec_reader)
	fl_dict = fill_dict(fl_reader) 
	
	#go through ec_dict (because it's bigger) and try to find corresponding value in fl_dict, if found – write to file
	for key in ec_dict:
		#first, check if the same city simply exists in the ec_dict
		if key in fl_dict:
			if ((len(fl_dict) == 1) and (len(ec_dict) == 1)):
				#no collisions 
				str_out = key + ',' + ','.join(ec_dict[key]) + ',' + ','.join(fl_dict[key]) + '\n'
				outfile.write(str_out)
			else:
				#handle collision. Look at all combinations of pairs (state, number) for this key
				for fl_p in fl_dict[key]:
					for ec_p in ec_dict[key]:
						fl_st, fl_num = fl_p
						ec_st, ec_num = ec_p
						if compare_states(fl_st, ec_st):
							str_out = key + ','+ ec_st + ',' + ec_num + ',' + fl_st + ',' + fl_num + '\n'
							outfile.write(str_out)
						
