from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def portfolio():
    return render_template('portfolio.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def web_page():
    return render_template('web_page.html')

app.run(debug=True)
