from pymongo import MongoClient
import pprint
import datetime
#connect to db
client = MongoClient('localhost', 27017)
db = client.web335
#update user document
result = db.users.update_one(
    {"employee_id":"0000008"},
    {
        "$set":{
            "email": "dltays@my.bellevue.edu"
        }
    }
)

#query the collection
pprint.pprint(db.users.find_one({"employee_id": "0000008"}, {'_id': 0, 'date_created': 0}))