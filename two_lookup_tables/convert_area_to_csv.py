with open('bls_lookup_sm.area', 'r') as fin, open('bls_lookup_sm.area.csv','w+') as fout:
	for line in fin:
		llist = line.split()
		id_str = llist[0]
		del llist[0]
		name =  " ".join(llist)
		lname = name.split(",")
		lname_clean = []
		for el in lname:
			lname_clean.append(el.strip())
		fout.write(id_str + ";" + ";".join(lname_clean) + "\n")
