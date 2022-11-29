from database.models.user_model import User
from database.init_db import get_database

USER_COLLECTION = "users"


class UserController():
    


    def __init__(self):
        database = get_database()
        users = database[USER_COLLECTION]
        self.db = users
        return  

    def authenticate(self, email, password):
        print(email, password)
        u = User(email, "", "", "", password, "")
        print(u.email, u.password)
        
        userDocument = self.db.find_one( {'email': u.email, 'password': u.password } )
        print("******* This is find_one: ", userDocument)
        if userDocument == None:
            return {
                'status_code': 400,
                'message': "Username or Password invalid"
            }   
        #need to check if username in db
        #db.getUser(username, args)
        #check pw
        #if false return object statuscode 404
        return {
            'status_code': 200,
            'message': "Username & Password valid"
        }

    
    def signup(self, email, username, firstName, lastName, password, birthday):
        print("IN SIGNUP FUNCTION:")
        u = User(username, firstName, lastName, password, email, birthday)
        userDocument = self.db.find_one( {'email': u.email})
        if userDocument != None:
            return {
                'status_code': 400,
                'message': "Email in use"
            }
        else:
            self.db.insert_one({'email': email, 'username': username, 'firstName': firstName, 'lastName': lastName, 'password': password, 'birthday': birthday})
        return {
            'status_code': 201,
            'message': "Created"
        }
            