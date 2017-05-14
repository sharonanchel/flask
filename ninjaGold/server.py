from flask import Flask, render_template, request, redirect, session
from random import randrange
import datetime

app = Flask(__name__)

app.secret_key = 'Sharon'

@app.route('/')
def index():

    if not 'gold' in session:
        session['gold'] = 0
        print session['gold']
    if not 'activity' in session:
        session['activity'] = []

    return render_template('index.html', gold=session['gold'], activity=session['activity'])


@app.route('/process_money', methods=['POST'])
def process():

    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day

    timestamp = datetime.date.today().strftime('%Y/%m/%d') + ' ' + datetime.datetime.now().strftime('%I:%M %p')

    if request.form['action'] == 'farm':
        pay = randrange(10,20)
        session['gold'] += pay
        print pay
        message = 'Earned ' + str(pay) + ' golds from the farm! (' + timestamp + ')'

    elif request.form['action'] == 'cave':
        pay = randrange(5,10)
        session['gold'] += pay
        message = 'Earned ' + str(pay) + ' golds from the cave! (' + timestamp + ')'

    elif request.form['action'] == 'house':
        pay = randrange(2,5)
        session['gold'] += pay
        message = 'Earned ' + str(pay) + ' golds from the house! (' + timestamp + ')'

    elif request.form['action'] == 'casino':
        pay = randrange(-50,50)
        session['gold'] += pay
        if pay > 0:
            message = 'Entered a casino and won '  + str(pay) + '  golds ... Nice! (' + timestamp + ')'
        else:
            message = 'Entered a casino and lost '  + str(pay) + '  golds ... Ouch! (' + timestamp + ')'

    if pay > 0:
        activity_text = (message, 'green')
    else:
        activity_text = (message, 'red')

    session['activity'].insert(0, activity_text)

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    del session['gold']
    del session['activity']
    return redirect('/')

app.run(debug = True)
