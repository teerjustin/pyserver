from database.models.user_model import User
from database.init_db import get_database

USER_COLLECTION = "users"


class UserController():
    


    def __init__(self):
        database = get_database()
        users = database[USER_COLLECTION]
        self.db = users
        return  

    def authenticate(self, username, password):
        print(username, password)
        u = User(username, password)
        print(u.username, u.password)

        if not self.db.find( {'username': u.username, 'password': u.password } ):
            return {
                'status_code': 400,
                'message': "Username or Password valid"
            }
        #need to check if username in db
        #db.getUser(username, args)
        #check pw
        #if false return object statuscode 404

        return {
            'status_code': 200,
            'message': "Username & Password valid"
        }

    
    def signup(self, username, first_name, last_name, password, email, birthday):
        u = User(username, first_name, last_name, password, email, birthday)
        