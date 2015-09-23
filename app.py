from flask import Flask, render_template

app = Flask(__name__)
data_path = 'data.csv'


@app.route('/')
def home():
	with open(data_path, 'rb') as doc:
		data = reader(doc)

	return render_template('index.html')


if __name__ == "__main__":
	app.run()