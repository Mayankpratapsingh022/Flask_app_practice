from flask import Flask

# here we are creating instance of the flask app
# whch is our WSGI(web server gateway interface ) application.

#  WSGI Application
app = Flask(__name__)

# this is a decorator
@app.route("/")
def welcome():

    return "Welcome to this Flask APP."




@app.route("/index")
def index():
    return "Welcome to the index page"




if __name__=="__main__":
    app.run(debug=True, port=8080)


