import os 

from flask import Flask, render_template, request, jsonify
from flask_dropzone import Dropzone

from . import extractor

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.register_blueprint(extractor.bp)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE = 'image',
    DROPZONE_MAX_FILE_SIZE = 3,
    DROPZONE_MAX_FILES = 1,
    DROPZONE_DEFAULT_MESSAGE = '<b>Drop files here<b><br>Or<br><button type="button" class="btn btn-outline-secondary btn-lg"> Upload Image </button>                ',
)

dropzone = Dropzone(app)

@app.route('/')
def extractor():
    return app

@app.route('/hello')
def hello():
    return 'Hello, World!'




     