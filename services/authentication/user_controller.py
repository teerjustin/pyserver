from database.models.user_model import User
from database.init_db import get_database
from bson.json_util import dumps, loads
import json

USER_COLLECTION = "users"


class UserController():
    

    def __init__(self):
        database = get_database()
        users = database[USER_COLLECTION]
        self.db = users
        return
    

    def get_all_users(self):
        users_list = []
        cursor = self.db.find()
        list_cursor = list(cursor)

        for document in list_cursor:
            #creating a User object from a database document
            user = User(document['email'], document['username'], document['firstName'], document['lastName'], document['password'], document['birthday'])
            #converting user object into json supported string
            user_as_string = user.toJson()
            #converting string into actual json serializible user object
            serialized_user = json.loads(user_as_string)
            users_list.append(serialized_user)

        return {
            'status_code': 200,
            'data': users_list
        }


    def authenticate(self, email, password):
        u = User(email, "", "", "", password, "")

        userDocument = self.db.find_one( {'email': u.email, 'password': u.password } )
        if userDocument == None:
            return {
                'status_code': 401,
                'message': "Unauthorized"
            }
        return {
            'status_code': 200,
            'message': "OK"
        }

    
    def signup(self, email, username, firstName, lastName, password, birthday):
        u = User(username, firstName, lastName, password, email, birthday)

        userDocument = self.db.find_one( {'email': u.email})
        if userDocument != None:
            return {
                'status_code': 400,
                'message': "Email in use"
            }
        
        self.db.insert_one({'email': email, 'username': username, 'firstName': firstName, 'lastName': lastName, 'password': password, 'birthday': birthday})
        return {
            'status_code': 201,
            'message': "Created"
        }

        