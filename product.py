from flask_restful import Resource, Api, request
from bson.objectid import ObjectId
import getData
import json


class Product(Resource):

    def __init__(self):
        self.collection = getData.collection

    def get(self, id):
        product = self.collection.find_one({"_id"  : ObjectId(id)})
        product["_id"] = str(product["_id"])
        return {'produit': product}

    def put(self, id):
        if request.method == "PUT":
            informations =  json.loads(request.data)
            id = { '_id': ObjectId(id) }
            modification = {'$set': {'titre': informations['titre'], 'price': informations['price'], 'description': informations['description']}}
            self.collection.update_one(id, modification)
        return {'id': str(id)}

    def delete(self, id):
        self.collection.delete_one({"_id": ObjectId(id)})
        return {'id': str(id)}

    def post(self):
        if request.method == "POST":
            informations =  json.loads(request.data)
            _id = self.collection.insert_one( {'titre': informations['titre'], 'price': informations['price'] , 'description': informations['description'] } )
        return { 'id' : str(_id.inserted_id) }