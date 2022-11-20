import random
from flask import Flask

rand_num = random.randint(0, 9)

app = Flask(__name__)

@app.route('/')
def guessnumber():
    #Rendering HTML Elements
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
        '<img src="https://media.giphy.com/media/l378khQxt68syiWJy/giphy-downsized-large.gif" width=200>'

@app.route("/<int:number>")
def userguess(number):
    if number > rand_num:
        return '<h1 style=color:Red>Too high, try again!</h1>' \
            '<img src="https://media.giphy.com/media/3og0IuWMpDm2PdTL8s/giphy-downsized-large.gif" width=200>'
    if number < rand_num:
        return '<h1 style=color:Blue>Too low, try again!</h1>' \
            '<img src="https://media.giphy.com/media/WUTxupKrZJMjver3UF/giphy.gif" width=200>'
    else:
        return '<h1 style=color:Green>You found it!</h1>' \
            '<img src="https://media.giphy.com/media/1hMk0bfsSrG32Nhd5K/giphy.gif" width=200>'

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)

