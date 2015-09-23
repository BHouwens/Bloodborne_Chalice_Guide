from flask import Flask, render_template
import csv

app = Flask(__name__)
data_path = 'data.csv'

def reader(path):
	reader = csv.DictReader(path, delimiter = ",")

	for row in reader:
		# do something with the csv row

@app.route('/')
def home():
	with open(data_path, 'rb') as doc:
		data = reader(doc)

	return render_template('index.html')


if __name__ == "__main__":
	app.run()