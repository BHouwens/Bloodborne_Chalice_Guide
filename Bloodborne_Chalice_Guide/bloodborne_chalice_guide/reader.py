import csv

'''
	Function to read the CSV and turn entries into usable data.
	It returns a list of dictionaries containing the chalice name as key and
	all other info as another list of dictionaries.
'''
def reader(doc):
		chalices = []
		reader = csv.DictReader(doc, delimiter = ",")

		for row in reader:
			'''
			Start by removing any stale entries under the same chalice
			'''
			for entry in chalices:
				if row["Chalice Used"] in entry.keys():
					chalices.remove(entry)

			details_list = [
							{"Timestamp" : row["Timestamp"]},
							{"Additional Rites" : row["Additional Rites"]},
							{"Chalice Glyph" : row["Chalice Glyph"]},
							{"Layer 1 (Weapons)" : row["Layer 1 (Weapons)"]},
							{"Layer 2 (Weapons)" : row["Layer 2 (Weapons)"]},
							{"Layer 3 (Weapons)" : row["Layer 3 (Weapons)"]},
							{"Layer 4 (Weapons)" : row["Layer 4 (Weapons)"]},
							{"Layer 1 (Materials)" : row["Layer 1 (Materials)"]},
							{"Layer 2 (Materials)" : row["Layer 2 (Materials)"]},
							{"Layer 3 (Materials)" : row["Layer 3 (Materials)"]},
							{"Layer 4 (Materials)" : row["Layer 4 (Materials)"]},
							]
			chalices.append({row["Chalice Used"] : details_list})

		return chalices