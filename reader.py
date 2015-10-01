import csv

class Chalice_Builder:

	def __init__(self, reader, path):
		'''
			Single chalice structure is as follows: 

			{
				'name' : 'Ailing Loran Root',
				'glyphs': [
					{
						'glyph': 'gh2z72rh',
						'layer1': [weapons, materials],
						'layer2': [weapons, materials],
						'notes': 'notes go here'
					}
				]
			}

		'''
		self.path = path

		if reader == 'first':
			self.chalices = self.first_reader(self.path)
		elif reader == 'second':
			self.chalices = self.second_reader(self.path)


	def first_reader(self, path):
		chalices = []

		with open(path, 'rb') as data:
			reader = csv.reader(data, delimiter=',')
			reader.next()

			for row in reader:
				if len(chalices) > 0:
					check = next((item for item in chalices if item["name"] == row[1]), None)

					if not check:
						new_chalice = self.create_chalice(row)
						chalices.append(new_chalice)
					else:
						new_glyph = self.create_glyph(row)
						
						index = next(index for (index, d) in enumerate(chalices) if d["name"] == row[1])
						chalices[index]['glyphs'].append(new_glyph)
				else:
					first_chalice = self.create_chalice(row)
					chalices.append(first_chalice)

		return chalices

	def second_reader(self, path):
		chalices = []

		with open(path, 'rb') as data:
			reader = csv.reader(data, delimiter=',')
			reader.next()

			for row in reader:
				if len(chalices) > 0:
					check = next((item for item in chalices if item["name"] == row[2]), None)



	def create_chalice(self, row):
		chalice = {
			'name' : row[1],
			'glyphs': []
		}

		new_glyph = self.create_glyph(row)
		chalice['glyphs'].append(new_glyph)

		return chalice


	def create_glyph(self, row):
		new_glyph = {}

		new_glyph['glyph'] = row[3]
		new_glyph['layer1'] = [ row[4], row[8] ]
		new_glyph['layer2'] = [ row[5], row[9] ]
		new_glyph['layer3'] = [ row[6], row[10] ]
		new_glyph['layer4'] = [ row[7], row[11] ]
		new_glyph['notes'] = row[12]

		return new_glyph



# Test Chalice_Builder ouput
if __name__ == "__main__":
	test = Chalice_Builder('data/first_data.csv')
	print test.chalices








