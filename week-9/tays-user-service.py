from pymongo import MongoClient
import pprint
import datetime
#connect to db
client = MongoClient('localhost', 27017)
db = client.web335

#create user
user = {
    "first_name": 'Clyde',
    "last_name": 'Drexler',
    "email": 'cdrexler@u.com',
    "employee_id": "0000008",
    "date_created": datetime.datetime.utcnow()
}
#insert user to db
user_id = db.users.insert_one(user).inserted_id

#print
print(user_id)
#query the collection
pprint.pprint(db.users.find_one({"employee_id": "0000008"}))

