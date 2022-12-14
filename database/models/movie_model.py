from ..init_db import get_database
import json


dbname = get_database()
collection_name = dbname["movies"]

class Movie():

    def __init__(self, imbd_id, imbd_link, title, imbd_score, genre, poster):
        self.imbd_id = imbd_id
        self.imbd_link = imbd_link
        self.title = title
        self.imbd_score = imbd_score
        self.genre = genre
        self.poster = poster


    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
