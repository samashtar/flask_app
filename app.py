from flask import Flask, render_template

# create a Flask instance of the app
app = Flask(__name__)


# create a route
@app.route('/')
# points to home.html
def index():
    return render_template('home.html')


# if the name matches - run the app - starting a server
# debug mode means app updates on save
if __name__ == '__main__':
    app.run(debug=True)
