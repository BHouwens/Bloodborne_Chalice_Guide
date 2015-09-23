import csv

def reader(path):
	'''
		Reads the csv in and attempts to construct a dict for 
		each chalice. Single chalice structure is as follows: 

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
	chalices = []

	with open(path, 'rb') as data:
		reader = csv.reader(data, delimiter=',')
		reader.next()

		for row in reader:
			if len(chalices) > 0:
				if row[1] not in chalices[:]:
					new_chalice = create_chalice(row)
					chalices.append(new_chalice)
					print 'New chalice created'
				else:
					new_glyph = {}

					new_glyph['glyph'] = row[3]
					new_glyph['layer1'] = [ row[4], row[8] ]
					new_glyph['layer2'] = [ row[5], row[9] ]
					new_glyph['layer3'] = [ row[6], row[10] ]
					new_glyph['layer4'] = [ row[7], row[11] ]
					new_glyph['notes'] = row[12]
					'New glyph is in'
					break
			else:
				first_chalice = create_chalice(row)
				chalices.append(first_chalice)
				print 'First chalice created'

		print chalices[5]



def create_chalice(row):
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

reader('data.csv')








