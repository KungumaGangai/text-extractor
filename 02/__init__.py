import os 

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_dropzone import Dropzone

from . import extractor

# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = 'key'
app.register_blueprint(extractor.bp)

dir_path = os.path.dirname(os.path.realpath(__file__))

app.config.update(
    UPLOADED_PATH=os.path.join(dir_path, 'static'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=1,
    DROPZONE_DEFAULT_MESSAGE = '<b>Drop files here<b><br>Or<br><button type="button" class="btn btn-outline-secondary btn-lg"> Upload Image </button>',
)
app.config['DROPZONE_REDIRECT_VIEW'] = 'makeMeme'

dropzone = Dropzone(app)

filename = None

@app.route('/')
def extractor():
    return app

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    global filename
    file = None
    if request.method == 'POST':
        f = request.files.get('file')
        file = f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
        filename = f.filename
    return render_template('index.html')

@app.route('/makeMeme', methods=['POST', 'GET'])
def makeMeme():
    global filename
    return render_template("index.html", file_name = filename)


@app.route('/hello')
def hello():
    return 'Hello, World!'




     