from flask import Flask, render_template
from reader import Chalice_Builder

app = Flask(__name__)
data_path = 'data/data.csv'


@app.route('/')
def home():
	raw_data = Chalice_Builder(data_path)
	chalices = []


	for item in raw_data.chalices:
		chalices.append(item['name'])


	return render_template('index.html',
		names=chalices,
		raw=['yebo'])


if __name__ == "__main__":
	app.run()