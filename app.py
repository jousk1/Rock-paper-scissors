from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)
app.config['DEBUG'] = True
API_KEY = ''

moves = ['rock', 'paper', 'scissors']


@app.route('/', methods =  ['GET', 'POST'])
def index():
    result = None  
    move = None

    if request.method == 'POST':
        move = request.form['move']
        computer_move = random.choice(moves)

        if move == computer_move:
            result =  "It's a tie!"
        elif (
            (move == "rock" and computer_move == "scissors") or
            (move == "paper" and computer_move == "rock") or
            (move == "scissors" and computer_move == "paper")
        ):
            result = f"You win! Your choice was {move}, and computer's was {computer_move}"
        else:
            result = f"Computer wins! Your choice was {move}, and computer's was {computer_move}"

    return render_template('index.html', result = result)

app.run()

