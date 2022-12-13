from database.init_db import get_database
from database.models.movie_model import Movie
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
