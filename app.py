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
		glyphs.append(item['glyphs'])


	return render_template('index.html',
		names=chalice_names,
		glyphs=glyphs)


if __name__ == "__main__":
	app.run()