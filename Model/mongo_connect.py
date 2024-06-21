from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# Connect to Database
ConcordiaEventManagementDB = client['ConcordiaEventManagementDB']