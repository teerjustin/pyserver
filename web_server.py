from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

USER = "master"
PW = "password"

@app.route("/homepage")
def index():
    print("here in home page")
    return render_template('loginAndReg.html')

@app.route("/login", methods = ["POST"])
def login():

    username = request.json['user']
    password = request.json['password']
    print("THIS IS MY USER: ", username)
    print("THIS IS MY PASSWORD: ", password)

    #
    if USER == username: 
        if PW == password:
            return { 'httpVers': 1.1, 'httpCode': 200, 'httpStatus': 'OK' }
    return { 'httpVers': 1.1, 'httpCode': 404, 'httpStatus': 'NOT_FOUND' }

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


@app.route("/healthcheck", methods=["GET"])
def liveliness():
    print("SERVER IS RUNNING: ")
    return '', 200


if __name__ == "__main__":
    app.run(debug=True)



