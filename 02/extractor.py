from PIL import Image
import pytesseract

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('extractor', __name__)

@bp.route('/')
def index():
    title = "TxtExt"
    return render_template('index.html', title=title)