from itertools import product
import unittest
from product import Product
from bson.objectid import ObjectId
import requests

class TestCRUD(unittest.TestCase):

    def setUp(self):
        self.collection = Product()

    def test_getOne(self):
        #  Avec cet Id nous sommes sencer recupérer le produit serviette
        product = self.collection.get(ObjectId('6274e9f88431e643175be6a7'))
        self.assertEqual(product['produit']['titre'], "serviette")

    def test_create(self):
        id = requests.post('http://127.0.0.1:5000/', json={'titre': 'nouveau produit', 'price': 456, 'description': 'On teste la création de produit'}).json()
        product = self.collection.get(ObjectId(id['id']))
        self.assertIsNotNone(product)

    def test_update(self):
        product = requests.put('http://127.0.0.1:5000/62752cb3c23b0ca4387c157f', json = {"titre": "produit modifié", "price": 20 , "description": "Nous modifions le produit"})
        self.assertEqual(product.status_code, 200)

    def test_delete(self):
        product = requests.delete('http://127.0.0.1:5000/6276210e7eb8afa716eaa261')
        self.assertEqual(product.status_code, 200)