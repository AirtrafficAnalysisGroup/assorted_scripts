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

def compare_strings(st1, st2):
	return (st1 == st2) or (st1 in st2) or (st2 in st1)

with open('bls_lookup_sm.area.csv', 'r') as ec_table, open('bts_filtered_3_col.csv', 'r') as fl_table, open('merged_lookup.csv', 'w+') as outfile:
	ec_reader = csv.reader(ec_table)
	fl_reader = csv.reader(fl_table, delimiter=';')
	ec_dict = fill_dict(ec_reader)
	fl_dict = fill_dict(fl_reader) 
	
	#go through ec_dict (because it's bigger) and try to find corresponding value in fl_dict, if found – write to file
	for ec_key in ec_dict:
		for fl_key in list(fl_dict):
			if compare_strings(ec_key, fl_key):
				if ((len(fl_dict) == 1) and (len(ec_dict) == 1)):
					#no collisions 
					str_out = ec_key + ',' + ','.join(ec_dict[ec_key]) + ',' + fl_key + ','  + ','.join(fl_dict[fl_key]) + '\n'
					outfile.write(str_out)
				else:
					#handle collision. Look at all combinations of pairs (state, number) for this ec_key
					for fl_p in fl_dict[fl_key]:
						for ec_p in ec_dict[ec_key]:
							fl_st, fl_num = fl_p
							ec_st, ec_num = ec_p
							if compare_strings(fl_st, ec_st):
								str_out = ec_key + ','+ ec_st + ',' + ec_num + ',' + fl_key + ',' + fl_st + ',' + fl_num + '\n'
								outfile.write(str_out)
						
