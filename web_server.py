from flask import Flask, render_template, request, redirect, session
# from services import UserController
import services.authentication.user_controller as uc
import services.movies.movie_controller as mc

app = Flask(__name__)



@app.route("/login", methods = ["POST"])
def login():
    email = request.json['email']
    password = request.json['password']

    u = uc.UserController()

    response = u.authenticate(email, password)
    print("Attempted to authenticate User %s with status %s", email, response['status_code'])
    return response


@app.route("/signup", methods=["POST"])
def signup():
    u = uc.UserController()
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']
    firstName = request.json['firstName']
    lastName = request.json['lastName']
    birthday = request.json['birthday']
    response = u.signup(email, username, firstName, lastName, password, birthday)
    print("Attempted to Signup User %s with status %s", email, response['status_code'])
    return response


@app.route("/healthcheck", methods=["GET"])
def liveliness():
    print("health-check PING, server is alive!")
    return {
        "status_code": 200,
        "data": "ding ding"
    }
    

@app.route("/getmovies", methods=["GET"])
def get_all_movies():
    print("i am going to attempt to get all movies")
    m = mc.MovieController()

    return m.get_all_movies()

@app.route("/getonemovie", methods=["GET"])
def get_one_movies():
    print("i am going to attempt to get ONE movie")
    test = "114709"
    test2 = "2"
    m = mc.MovieController()
    
    return m.get_one_movie(test)



if __name__ == "__main__":
    app.run(debug=True)






    #
    # front end will hit this endpoint at localhost:port
    # 1. act as a ping

    # form that has username and password
    # pass user / pw from form and print that here --> frontend makes a request
    # access request here
    # POST /login localhost:port
    # requests.get(user)

    # if userr == const user
    # and password == const pass
    # success, 200 
    # else, 404
    # if username == USER: 
    #     print('username is == to user')