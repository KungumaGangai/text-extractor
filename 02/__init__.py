import os 

from flask import Flask
from flask_dropzone import Dropzone
# from flask_uploads import UploadSet
# , configure_uploads, IMAGES, patch_request_class
from . import extractor

app = Flask(__name__)
app.register_blueprint(extractor.bp)



# Uploads settings
# app.config['UPLOAD_PHOTOS_DEST'] = os.getcwd() + '/uploads'

# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)
# patch_request_class(app) #set maximum file size, default is 16MB

@app.route('/')
def extractor():
    dropzone = Dropzone(app)

    # Dropzone Settings
    app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
    app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
    app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
    app.config['DROPZONE_REDIRECT_VIEW'] = 'results'
    return app

@app.route('/hello')
def hello():
    return 'Hello, World!'




     