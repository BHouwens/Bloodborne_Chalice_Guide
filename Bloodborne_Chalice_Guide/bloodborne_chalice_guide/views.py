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

	info["chalices"] = context

	return info