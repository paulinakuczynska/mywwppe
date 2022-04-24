from os import environ
from pathlib import Path

class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY') or 'something'
    UPLOAD_FOLDER = Path('app', 'uploads')
    ALLOWED_EXTENSIONS = {'pptx'}