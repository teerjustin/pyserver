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
    print("SERVER IS RUNNING: ")
    m = mc.MovieController()

    # m.read_movies()
    return 'done'


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