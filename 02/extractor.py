import os

from flask import current_app
from PIL import Image
from flask_dropzone import Dropzone
import pytesseract

from flask import (
    Blueprint, app, flash, g, redirect, render_template, request, session, url_for, jsonify
)

bp = Blueprint('extractor', __name__)

# dir_path = os.path.dirname(os.path.realpath(__file__))

# current_app.config.update(
#     UPLOADED_PATH=os.path.join(dir_path, 'static'),
#     # Flask-Dropzone config:
#     DROPZONE_ALLOWED_FILE_TYPE='image',
#     DROPZONE_MAX_FILE_SIZE=3,
#     DROPZONE_MAX_FILES=1,
#     DROPZONE_DEFAULT_MESSAGE = '<b>Drop files here<b><br>Or<br><button type="button" class="btn btn-outline-secondary btn-lg"> Upload Image </button>',
# )
# current_app.config['DROPZONE_REDIRECT_VIEW'] = 'makeMeme'

# dropzone = Dropzone(current_app)

# filename = None

@bp.route('/')
def index():
    title = "TxtExt"
    return render_template('index.html', title=title)

# @bp.route('/upload', methods=['POST', 'GET'])
# def upload():
#     global filename
#     file = None
#     if request.method == 'POST':
#         # return "Hit!"
#         f = request.files.get('file')
#         file = f.save(os.path.join(current_app.config['UPLOADED_PATH'], f.filename))
#         filename = f.filename
#     return render_template('index.html')

# @bp.route('/makeMeme', methods=['POST', 'GET'])
# def makeMeme():
#     global filename
#     return render_template("makeMeme.html", file_name = filename)

