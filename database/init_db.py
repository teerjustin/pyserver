import pymongo
import certifi


ca = certifi.where()
DB_NAME = 'test'

def get_database():
   print("in here")
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://JustinTeer:JustinTeer123@cluster0.jd0xczb.mongodb.net/test"
   client = pymongo.MongoClient(CONNECTION_STRING, tlsCAFile=ca)
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   # client = MongoClient(CONNECTION_STRING)
   # Create the database for our example (we will use the same database throughout the tutorial
   print("This is client: ", client)
   return client[DB_NAME]
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
