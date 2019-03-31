import os
from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from os import environ

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/upload', methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("photo"):
        filename = file.filename
        destination = '/'.join([target, filename])
        file.save(destination)

    return redirect(url_for('send_image', filename=filename))


@app.route('/img/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


if __name__ == '__main__':
    app.run(debug=False, port=environ.get("PORT", 5000), processes=2)
