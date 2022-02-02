import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vlpot.mongodb.net/students"

cluster = MongoClient(url)
db = cluster.pytech
students = db.students

docs = db.students.find({})

for results in docs:
    print(results)

john = {
    "student_id" : "1010",
    "first_name": "John",
    "last_name": "Doe"
}
john_student_id = students.insert_one(john).inserted_id

newDoc = students.find_one({"student_id":"1010"})
print(newDoc)