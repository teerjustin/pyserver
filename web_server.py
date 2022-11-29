from flask import Flask, render_template, request, redirect, session
# from services import UserController
import services.authentication.user_controller as uc

app = Flask(__name__)

USER = "master"
PW = "password"

@app.route("/homepage")
def index():
    print("here in home page")
    return render_template('loginAndReg.html')

@app.route("/login", methods = ["POST"])
def login():
    email = request.json['email']
    password = request.json['password']
    print("THIS IS MY USERS EMAIL: ", email)
    print("THIS IS MY PASSWORD: ", password)

    u = uc.UserController()

    print('hi')
    response = u.authenticate(email, password)
    return response

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
    return response


@app.route("/healthcheck", methods=["GET"])
def liveliness():
    print("SERVER IS RUNNING: ")
    return '', 200


if __name__ == "__main__":
    app.run(debug=True)



