from ..init_db import get_database
import json

dbname = get_database()
collection_name = dbname["users"]



class User():

    def __init__(self,  email, username, first_name, last_name, password, birthday):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birthday = birthday

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
    
