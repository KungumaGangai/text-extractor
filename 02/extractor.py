import os
# from flask_dropzone import Dropzone
from PIL import Image
import pytesseract

from flask import (
    Blueprint, app, flash, g, redirect, render_template, request, session, url_for, jsonify
)

bp = Blueprint('extractor', __name__)

@bp.route('/')
def index():
    title = "TxtExt"
    return render_template('index.html', title=title)

@bp.route('/success')
def success():
    return "image uploaded!"

@bp.route('/upload', methods=['POST', 'GET'])
def upload():
    # if request.method == 'POST':        
    #     f = request.files.get('file')
    #     file_path = os.path.join(app.config['UPLOADED_PATH'], f.filename)
    #     f.save(file_path)
    #     # You can return a JSON response then get it on client side:
    #     # (see template index.html for client implementation)
    #     # return jsonify(uploaded_path=file_path)
    #     return render_template('index.html')

    if request.method == 'POST':
        for f in request.files.getlist('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return redirect(url_for('extractor.success'))
