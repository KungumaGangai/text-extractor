import os

from PIL import Image
import pytesseract

from flask import (
    Blueprint, app, flash, g, redirect, render_template, request, session, url_for, jsonify
)

bp = Blueprint('extractor', __name__)

dir_path = os.path.dirname(os.path.realpath(__file__))

@bp.route('/')
def index():
    title = "TxtExt"
    return render_template('index.html', title=title)

@bp.route('/extracttext')
def extracttext():
    file_name = request.args['file_name']
       
    pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"    
    image_path = r"E:/gitprojects/text-extractor/02/static/"+file_name
    image = Image.open(image_path)
    txt_from_img = pytesseract.image_to_string(image)
    
    return render_template('processed_image.html', file_name=file_name, extractedtext=txt_from_img)

@bp.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        content = request.form['edittext']
        doc = open('E:/gitprojects/text-extractor/02/static/extracted.txt', 'w')
        doc.write(content)
        doc.close()
        return render_template('makeMeme.html', content=content)
    

