from ..init_db import get_database

dbname = get_database()
collection_name = dbname["users"]



class User():

    def __init__(self, username, password, first_name='test', last_name='test', email='test', birthday='test'):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birthday = birthday

