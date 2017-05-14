from flask import Flask, render_template, request, redirect, session, flash
from random import randrange
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if session.get('win', None) == None:
        print 'hei'
        session['win'] = 0
    if session.get('loss', None) == None:
        session['loss'] = 0
    if session.get('tie', None) == None:
        session['tie'] = 0
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    randomNum = randrange(1,4)
    print randomNum
    # throw = request.form.get('throw', None)
    if 'rock' in request.form:
        userNum = 1
    elif 'paper' in request.form:
        userNum = 2
    else:
        userNum = 3

    if (userNum == randomNum): # covers all ties
        session['outcome'] = 'You tied bro'
        session['tie'] += 1
    elif (userNum == 1 and randomNum == 2): # rock lose pa
        session['outcome'] = "Your rock lost to computer's paper"
        session['loss'] += 1
    elif (userNum == 1 and randomNum == 3): # rock win sc
        session['outcome'] = "Your rock won against computer's scissors"
        session['win'] += 1
    elif (userNum == 2 and randomNum == 1): # paper win ro
        session['outcome'] = "Your paper won against computer's rock"
        session['win'] += 1
    elif (userNum == 2 and randomNum == 3): # paper lose sci
        session['outcome'] = "Your paper lost to computer's scissors"
        session['loss'] += 1
    elif (userNum == 3 and randomNum == 1): # scissors loses ro
        session['outcome'] = "Your scissors lost against computer's rock"
        session['loss'] += 1
    elif (userNum == 3 and randomNum == 2): # scissors wins to paper
        session['outcome'] = "Your scissors won against computer's paper"
        session['win'] += 1
    # 1 - rock
    # 2 - paper
    # 3 - scissors
    return redirect('/')

app.run(debug = True)
