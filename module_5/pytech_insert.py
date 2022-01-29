import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vlpot.mongodb.net/students"

cluster = MongoClient(url)
db = cluster.pytech
students = db.students

thorin = {
    "student_id" : "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield"
}

thorin_student_id = students.insert_one(thorin).inserted_id
print(thorin_student_id)

bilbo = {
    "student_id" : "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins"
}
bilbo_student_id = students.insert_one(bilbo).inserted_id
print(bilbo_student_id)

frodo = {
    "student_id" : "1009",
    "first_name": "Frodo",
    "last_name": "Baggins"
}
frodo_student_id = students.insert_one(frodo)
print(frodo_student_id)