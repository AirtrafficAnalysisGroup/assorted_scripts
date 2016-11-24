#for bts_filtered (duh)

with open('bts_filtered.csv', 'r') as fin, open('bts_filtered_3_col.csv','w+') as fout:
	for line in fin:
		clean_line = line.replace("\"", "")
		llist = clean_line.split(",")
		outlist = []
		for el in llist:
			el1 = el.strip()
			el2 = el1.replace("/","-")
			outlist.append(el2)
		fout.write(";".join(outlist)+"\n")
