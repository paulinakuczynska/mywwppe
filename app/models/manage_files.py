from flask import flash
from app import app
from os import rename, mkdir
from pathlib import Path
from shutil import unpack_archive, make_archive

def prepare_file_for_editing(file, new_name):
    
    uploaded_file = Path(app.config['UPLOAD_FOLDER'], file)
    new_filename = Path(app.config['UPLOAD_FOLDER'], new_name)
    new_dir = Path(app.config['UPLOAD_FOLDER'], 'new')
    
    if Path.is_file(uploaded_file):
        rename(uploaded_file, new_filename)
        mkdir(new_dir)
        unpack_archive(new_filename, new_dir, 'zip')
    else:
        flash('No file to customization')

def prepare_file_for_user(name):

    file_for_user = Path(app.config['UPLOAD_FOLDER'], name)
    new_dir = Path(app.config['UPLOAD_FOLDER'], 'new')

    if Path.is_file(Path(new_dir, '[Content_Types].xml')):
        make_archive(Path(app.config['UPLOAD_FOLDER'], 'zipped'), 'zip', new_dir)
        rename(Path(app.config['UPLOAD_FOLDER'], 'zipped.zip'), file_for_user)
    else:
        flash('No file to download')