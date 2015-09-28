from flask import Flask, render_template
from reader import Chalice_Builder

app = Flask(__name__)
data_path = 'data/data.csv'


@app.route('/')
def home():
	raw_data = Chalice_Builder(data_path)
	chalice_names = []
	glyphs = []


	for item in raw_data.chalices:
		chalice_names.append(item['name'])

		for a in item['glyphs']:
			glyph_entry = {}

			glyph_entry['name'] = item['name']
			glyph_entry['glyph'] = a['glyph']
			glyph_entry['layer1'] = a['layer1'][1]
			glyph_entry['layer2'] = a['layer2'][1]
			glyph_entry['layer3'] = a['layer3'][1]
			glyph_entry['layer4'] = a['layer4'][1]
			glyph_entry['notes'] = a['notes'].decode("utf8")
		
			glyphs.append(glyph_entry)

	return render_template('index.html',
		names=chalice_names,
		glyphs=glyphs)


if __name__ == "__main__":
	app.run(debug=True)