from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def main():
    return 'No Ninjas here'

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<ninja_color>')
def color(ninja_color):
    if ninja_color == "blue":
        image = 'img/leonardo.jpg'
    elif ninja_color == "purple":
        image = 'img/donatello.jpg'
    elif ninja_color == "orange":
        image = 'img/raphael.jpg'
    elif ninja_color == "red":
        image = 'img/michelangelo.jpg'
    elif ninja_color == "black":
        image = 'img/notapril.jpg'
    else:
        image = 'img/tmnt.png'

    return render_template('color.html', ninja_color=ninja_color, image=image)

# @app.route('/ninja/blue')
# def blue():
#     return render_template('blue.html')
#
# @app.route('/ninja/red')
# def red():
#     return render_template('red.html')

app.run(debug=True)
