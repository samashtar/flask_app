import os
from flask import Flask, render_template, request, send_from_directory, redirect, url_for

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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
