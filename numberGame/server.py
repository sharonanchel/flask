from flask import Flask, render_template, session, redirect, request, flash
from random import randrange
app = Flask(__name__)

app.secret_key = 'sharon'

@app.route('/')
def main():

    if not 'numToGuess' in session:
        session['numToGuess'] = randrange(0,100)
        print session['numToGuess']
        session['outcome'] = ''
        session['guessCount'] = 0
    return render_template('main.html', outcome=session['outcome'], numToGuess=session['numToGuess'], guessCount=session['guessCount'])

@app.route('/process', methods=['POST'])
def process():
    guess = request.form['guess']

    session['guessCount'] +=1

    print guess

    if int(guess) > 100 or int(guess) < 0:
        session['outcome'] = 'Please enter a number between 1 and 100'
    elif int(guess) == int(session['numToGuess']):
        session['outcome'] = 'was the number!'
    elif int(guess) < int(session['numToGuess']):
        session['outcome']  = 'Too low!'
    elif int(guess) > int(session['numToGuess']):
        session['outcome'] = 'Too high!'

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    del session['numToGuess']
    return redirect('/')

app.run(debug=True)
