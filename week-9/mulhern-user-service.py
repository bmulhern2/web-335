#Title: Assignment 9.2
#Author: Professor Krasso, MongoDB
#Date: 22 June 2020,
#Modified By: Brendan Mulhern,
#Description: Connecting to MongoDB using PyMongo.
from pymongo import MongoClient
from pprint import pprint
from datetime import datetime

client = MongoClient("mongodb+srv://bmulhern2:Bmole22%21%21@cluster0-eopst.mongodb.net/web335?retryWrites=true&w=majority")
db = client.web335
user = {
    "first_name": "Doug",
    "last_name": "Sandberg",
    "email": "dsandberg@hg.com",
    "employee_id": "007200494",
    "date_created": datetime.utcnow()
}
user_id = db.users.insert_one(user).inserted_id
pprint(db.users.find_one({"employee_id": "007200494"}))
