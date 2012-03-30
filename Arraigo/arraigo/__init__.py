from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import NewRequest

from gridfs import GridFS
import pymongo


def main(global_config, **settings):
	config = Configurator(settings=settings)
	config.add_static_view('static', 'static', cache_max_age=3600)

	db_uri = settings['db_uri']
	conn = pymongo.Connection(db_uri)
	config.registry.settings['db_conn'] = conn
	config.add_subscriber(add_mongo_db, NewRequest)

	config.add_route('home', '/')
	# other routes and more config...
	config.scan('arraigo')

	return config.make_wsgi_app()

def add_mongo_db(event):
    settings = event.request.registry.settings
    db = settings['db_conn'][settings['db_name']]
    event.request.db = db
    event.request.fs = GridFS(db)