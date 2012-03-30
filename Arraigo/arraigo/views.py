from pyramid.view import view_config

@view_config(route_name='home', renderer="arraigo:templates/home.pt")
def home(request):
	representantes = request.db['representantes'].find()
	return {'representantes':representantes}