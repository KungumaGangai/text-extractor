from flask import Flask
from . import extractor

app = Flask(__name__)
app.register_blueprint(extractor.bp)

@app.route('/')
def extractor():
    return app

@app.route('/hello')
def hello():
    return 'Hello, World!'




     