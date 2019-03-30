import os
from flask import Flask, render_template, request

app = Flask(__name__, static_folder="images")

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

    return render_template('photo.html', image=filename)


# @app.route('/photo')
# def show():
#     full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')
#     return render_template("home.html", user_image=full_filename)


if __name__ == '__main__':
    app.run(debug=True)
