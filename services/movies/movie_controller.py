from database.init_db import get_database
from database.models.movie_model import Movie
from bson.json_util import dumps, loads
import json
import csv


MOVIE_COLLECTION = "movies"
MOVIE_PATH = "/Users/teerjustin/Desktop/2022projects/archive/MovieGenre.csv"

class MovieController():
    
    def __init__(self):
        database = get_database()
        movies = database[MOVIE_COLLECTION]
        self.db = movies
        return

    def read_movies(self):
        print("insert movie function ***********************")
        
        with open(MOVIE_PATH, 'r', encoding = "ISO-8859-1") as csv_file:
            # heading = next(csv_file)

            reader = csv.DictReader(csv_file, delimiter=',')

            for row in reader:
                self.db.insert_one({'imbd_id': row['id'], 'imbd_link': row['link'], 'title': row['title'], 'imbd_score': row['score'], 'genre': row['genre'], 'poster': row['poster']})
        
        csv_file.close()
        return

    def get_all_movies(self):
        movies_list = [];
        cursor = self.db.find({}).limit(40)
        list_cursor = list(cursor)

        for document in list_cursor:
            movie = Movie(document['imbd_id'], document['imbd_link'], document['title'], document['imbd_score'], document['genre'], document['poster'])
            movie_as_string = movie.toJson()
            #converting string into actual json serializible user object
            serialized_movie = json.loads(movie_as_string)
            movies_list.append(serialized_movie)

        return {
            'status_code': 200,
            'data': movies_list[:20]
        }
    
    def get_one_movie(self, imbd_id):
        print("inside get one function")
        print("this is imbd id: ", imbd_id)

        movie = self.db.find_one( {'imbd_id': imbd_id} )
        if movie:
            movie_obj = Movie(movie['imbd_id'], movie['imbd_link'], movie['title'], movie['imbd_score'], movie['genre'], movie['poster'])
            movie_as_string = movie_obj.toJson()
            serialized_movie = json.loads(movie_as_string)

            return {
                'status': 200,
                'data': serialized_movie
            }

        return {
            'status': 400
        }
    
