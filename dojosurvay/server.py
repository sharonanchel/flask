from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=["POST"])
def submit():
    name = request.form["name"]
    location = request.form["location"]
    languages = request.form["languages"]
    comment = request.form["comment"]
    return render_template('result.html',name=name,location=location,languages=languages,comment=comment)

app.run(debug=True)
