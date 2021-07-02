import os
import img2pdf
import pytesseract

from PIL import Image
from fpdf import FPDF


from flask import (
    Blueprint, app, flash, g, redirect, render_template, request, session, url_for, jsonify, send_file
)

bp = Blueprint('extractor', __name__)

dir_path = os.path.dirname(os.path.realpath(__file__))

file_name = None


@bp.route('/')
def index():
    title = "TxtExt"
    return render_template('index.html', title=title)

@bp.route('/extracttext')
def extracttext():
    global file_name 
    file_name = request.args['file_name']
       
    pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"    
    image_path = r"E:/gitprojects/text-extractor/02/static/"+file_name
    image = Image.open(image_path)
    txt_from_img = pytesseract.image_to_string(image)
    
    return render_template('processed_image.html', file_name=file_name, extractedtext=txt_from_img)

@bp.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        # using img2pdf library
        img_path = r"E:/gitprojects/text-extractor/02/static/"+file_name
        pdf_path = r"E:/gitprojects/text-extractor/02/static/data1.pdf"
        image = Image.open(img_path)
        pdf_bytes = img2pdf.convert(image.filename)
        file = open(pdf_path, "wb")
        file.write(pdf_bytes)
        image.close()
        file.close()

        # export as .txt file
        content = request.form['edittext']
        doc = open('E:/gitprojects/text-extractor/02/static/extracted.txt', 'w')
        doc.write(content)
        doc.close()

        # export as pdf process
        # pdf = FPDF()
        # pdf.add_page()
        # pdf.set_font('Arial', size=15)
        # # pdf.cell(200, 10, txt=content, ln=1, align='C')
        # for x in content:
        #     pdf.cell(200, 10, txt = x, ln = 1, align = 'C')   
        # pdf.output("IMG.pdf")
        

        return render_template('makeMeme.html', content=content)
    

