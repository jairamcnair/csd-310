import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vlpot.mongodb.net/students"

cluster = MongoClient(url)
db = cluster.pytech
students = db.students

doc1 = db.students.find({})

for result in doc1:
    print(result)

doc2 = db.students.find_one({"student_id":"1008"})
print(doc2)
