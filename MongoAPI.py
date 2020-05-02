from pymongo import MongoClient


client = MongoClient(port=27017)

""" Implementation of Database store """
class MongoAPI:
    
    def __init__(self, database):
        self._database = database

    # create database
    def create_db(self):
        pass

    # delete database 
    def delete_db(self):
        pass

    # create collection
    def create_collection(self):
        pass

    # delete collection
    def delete_collection(self):
        pass

    # create document
    def create_document(self):
        pass

    # delete document
    def delete_document(self):
        pass

    # edit document
    def edit_document(self):
        pass

    # find document
    def find_document(self):