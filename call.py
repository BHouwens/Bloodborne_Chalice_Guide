from reader import reader

path = "Chalice Dungeon Submission Form (Responses) - Form Responses 1.csv"
with open(path, "rb") as obj:
	chalices = reader(obj)

	for entry in chalices:
		print entry.keys()