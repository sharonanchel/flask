from flask import Flask, render_template  # Import Flask to allow us to create our app.
                         # render_template to allow us to render index.html.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
# @app.route('/success')
# def success():           # The "@" symbol designates a "decorator" which attaches the following
#    return render_template('success.html')# function to the '/' route. This means that whenever we send a request to

@app.route('/')
def main():           # The "@" symbol designates a "decorator" which attaches the following
   return render_template('main.html')

@app.route('/left')
def left():           # The "@" symbol designates a "decorator" which attaches the following
   return render_template('left.html')

@app.route('/right')
def right():           # The "@" symbol designates a "decorator" which attaches the following
   return render_template('right.html')

@app.route('/red')
def round_red_door():           # The "@" symbol designates a "decorator" which attaches the following
   return render_template('round_red_door.html')

@app.route('/black')
def tall_black_door():           # The "@" symbol designates a "decorator" which attaches the following
   return render_template('tall_black_door.html')
                         # localhost:5000/ we will run the following "hello_world" function.
# @app.route('/success')
# def other_function():           # The "@" symbol designates a "decorator" which attaches the following
#    return render_template('success.html')# function to the '/' route. This means that whenever we send a request to
# # def hello_world():
# #   return render_template('index.html')  # Render the template and return it!
app.run(debug=True)
