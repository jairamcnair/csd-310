import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vlpot.mongodb.net/students"

cluster = MongoClient(url)
db = cluster.pytech
students = db.students

docs = db.students.find({})

for results in docs:
    print(results)


result = db.students.update_one({"student_id":"1007"}, {"$set":{"last_name":"Smith"}})

doc2 = students.find_one({"student_id":"1007"})
print(doc2)









