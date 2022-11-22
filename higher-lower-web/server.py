from flask import Flask

app = Flask(__name__)

@app.route("/")
def guessinggame():
    return "<h1>Guess a number between 0 and 9"