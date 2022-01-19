from pymongo import MongoClient
from bson.objectid import ObjectId
import json
 
class AnimalShelter(object):
    def __init__(self, username, password):
    #Initialize the MongoClient
        self.client = MongoClient('mongodb://%s:%s@localhost:33671/?authSource=AAC' % (username, password))
        self.database = self.client['AAC']
  
#Create method
    def create(self, data=dict()):
        if data is not None:
            self.database.animals.insert_one(data) #data should be dictionary
        else:
            raise Exception("Nothing to save, because data parameter is empty")
          
#retrieve method
    def read(self, data):
        if data is not None:
            return self.database.animals.find(data,{"_id":False}) #data should be dictionary
        else:
            raise Exception("Nothing to return, because data parameter is empty")

#Update method
    def update(self, find=dict(), replace=dict()):
        if find is not None:
            x = self.database.animals.update_many(find, {"$set":replace}) #data should be dictionary
            return json.dumps(x)
        else:
            raise Exception("Nothing to update, because data parameter is empty")
          
#Delete method
    def delete(self, data=dict()):
        if data is not None:
            return json.dumps(self.database.animals.remove(data))
        else:
            raise Exception("Nothing to delete, because data parameter is empty")