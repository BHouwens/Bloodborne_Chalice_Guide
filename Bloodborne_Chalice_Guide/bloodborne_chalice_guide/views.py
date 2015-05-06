from pyramid.view import view_config
from reader import reader


@view_config(route_name='home',
			 renderer='templates/home.jinja2')
def home(request):
	info = {}
	path = "form.csv"


	'''
	  Opens CSV and reads to a list
	'''
	with open(path, "rb") as obj:
		context = reader(obj)

	'''
	  Pull first value out and stick it in a variable.
	  For loop is the only way to pull first value from a dict.
	'''
	first_entry = context[0]
	first_value = []

	for value in first_entry.values():
		first_value = value

	'''
	  Add headings from first_value into a new variable
	'''
	headings = []

	for entry in first_value:
		for key in entry.keys():
			headings.append(key)


	info["chalices"] = context
	info["headings"] = headings

	return info