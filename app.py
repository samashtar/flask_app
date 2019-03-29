from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return filename


if __name__ == '__main__':
    app.run(debug=True)
