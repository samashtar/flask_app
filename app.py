from flask import Flask

# create a Flask instance of the app
app = Flask(__name__)

# if the name matches - run the app - starting a server
if __name__ == '__main__':
    app.run()
