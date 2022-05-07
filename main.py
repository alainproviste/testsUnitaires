from flask_restful import Resource, Api, request
from flask import Flask
from product import Product

app = Flask(__name__)
api = Api(app)

api.add_resource(Product, '/' ,'/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)