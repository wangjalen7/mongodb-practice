import os
from pymongo import MongoClient

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.q0nrosd.mongodb.net/"
client = MongoClient(uri, username='zac9nk', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)

# create new collection
db = client['lab_9']  
collection = db['lab9_collection'] 

# inserts five (5) documents
documents = [
    {"name": "John Doe", "age": 30, "hobby": "cycling"},
    {"name": "Jane Smith", "age": 25, "hobby": "hiking"},
    {"name": "Alice Johnson", "age": 35, "hobby": "swimming"},
    {"name": "Bob Brown", "age": 40, "hobby": "cooking"},
    {"name": "Carol White", "age": 22, "hobby": "running"}
]
result = collection.insert_many(documents)
print("Documents inserted, IDs:", result.inserted_ids)

# query to display exactly three (3) of those documents
for doc in collection.find().limit(3):
    print(doc)

client.close()
