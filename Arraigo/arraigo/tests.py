import unittest

from pyramid import testing
from arraigo.models import Representante
from mongoengine import *



class RepresentanteTests(unittest.TestCase):
	def setUp(self):
		connect('arraigo_test')

	def tearDown(self):
		for representante in Representante.objects:
			representante.delete()

	def test_create_a_parlamentarian(self):
		representante = Representante(name='el Representante')
		representante.save()
		self.assertEqual(len(Representante.objects), 1)

	def test_create_a_representante_without_a_name(self):
		representante = Representante()
		with self.assertRaises(ValidationError):
			representante.save()

	def test_create_a_representante_with_an_empty_name(self):
		representante = Representante(name="")
		with self.assertRaises(ValidationError):
			representante.save()