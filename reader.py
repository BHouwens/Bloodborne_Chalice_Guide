import csv

class Chalice_Builder:

	def __init__(self, path):
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
		self.chalices = []

		with open(path, 'rb') as data:
			reader = csv.reader(data, delimiter=',')
			reader.next()

			for row in reader:
				if len(self.chalices) > 0:
					check = next((item for item in self.chalices if item["name"] == row[1]), None)

					if not check:
						new_chalice = self.create_chalice(row)
						self.chalices.append(new_chalice)
					else:
						new_glyph = {}

						new_glyph['glyph'] = row[3]
						new_glyph['layer1'] = [ row[4], row[8] ]
						new_glyph['layer2'] = [ row[5], row[9] ]
						new_glyph['layer3'] = [ row[6], row[10] ]
						new_glyph['layer4'] = [ row[7], row[11] ]
						new_glyph['notes'] = row[12]
						
						index = next(index for (index, d) in enumerate(self.chalices) if d["name"] == row[1])
						self.chalices[index]['glyphs'].append(new_glyph)
				else:
					first_chalice = self.create_chalice(row)
					self.chalices.append(first_chalice)



	def create_chalice(self, row):
		chalice = {
			'name' : row[1],
			'glyphs': []
		}

		new_glyph = {}

		new_glyph['glyph'] = row[3]
		new_glyph['layer1'] = [ row[4], row[8] ]
		new_glyph['layer2'] = [ row[5], row[9] ]
		new_glyph['layer3'] = [ row[6], row[10] ]
		new_glyph['layer4'] = [ row[7], row[11] ]
		new_glyph['notes'] = row[12]

		chalice['glyphs'].append(new_glyph)

		return chalice

if __name__ == "__main__":
	test = Chalice_Builder('data/data.csv')
	print test.chalices








