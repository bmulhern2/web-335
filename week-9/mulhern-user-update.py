#Title: Assignment 9.2
#Author: Professor Krasso, MongoDB
#Date: 22 June 2020,
#Modified By: Brendan Mulhern,
#Description: Updating Users With MongoDB using PyMongo.
from pymongo import MongoClient
import pprint
import datetime

client = MongoClient("mongodb+srv://bmulhern2:Bmole22%21%21@cluster0-eopst.mongodb.net/web335?retryWrites=true&w=majority")
db = client.web335
out = db.users.update_one(
    {"employee_id":"007200494"},
    {
        "$set":{
            "email": "bmulhern@my365.bellevue.edu"
        }
    }
)
pprint.pprint(db.users.find_one({"employee_id": "007200494"}))