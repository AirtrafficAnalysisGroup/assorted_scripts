#for market table and a lookup table returns a csv with only US aggregated markets
import csv

def main():
	lookup_path = "lookup_market.asp"
	table_path = "313048317_T_DB1B_MARKET.csv"
	in_table = set()
	table = open(table_path, 'r')
	lookup = open(lookup_path, 'r')
	table_rows = csv.reader(table, quoting=csv.QUOTE_NONNUMERIC)
	lookup_rows = csv.reader(lookup)
	next(table_rows) #skip the header
	next(lookup_rows)
	lookup_dict = {}
	for lookup_row in lookup_rows:
		lookup_dict[float(lookup_row[0])] = lookup_row[1]
	for table_row in table_rows:
		lookup.seek(0)
		next(lookup_rows) #skip the header
		if table_row[2] != "US":
			continue
		if table_row[1] in lookup_dict:
			in_table.add((table_row[1], lookup_dict[table_row[1]]))

	with open("filtered.csv", 'w+') as outfile:
		output_writer = csv.writer(outfile)
		for el in in_table:
			output_writer.writerow(el)

if __name__ == "__main__":
	main()
