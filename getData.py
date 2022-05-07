from http import client
import pymongo
import urllib

con = pymongo.MongoClient("mongodb+srv://user:" + urllib.parse.quote("P@ssword1234") + "@cluster0.gzidn.mongodb.net/mydatabase?retryWrites=true&w=majority")

db = con.get_database("mydatabase")
collection = db.product