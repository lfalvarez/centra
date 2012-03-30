from mongoengine import *

class Representante(Document):
	name = StringField(required=True, min_length=1)