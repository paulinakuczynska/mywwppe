from flask import flash
from app import app
from os import rename, mkdir, listdir, path, unlink
from pathlib import Path
from shutil import unpack_archive, make_archive, rmtree

class Files:
    newdir = Path(app.config['UPLOAD_FOLDER'], 'new')
    endfile = Path(app.config['UPLOAD_FOLDER'], 'new.pptx')

    def __init__(self, filename, newname):
        self.filename = Path(app.config['UPLOAD_FOLDER'], filename)
        self.newname = Path(app.config['UPLOAD_FOLDER'], newname)

    def prepare_file_for_editing(self): 
        if Path.is_file(self.filename):
            rename(self.filename, self.newname)
            mkdir(self.newdir)
            unpack_archive(self.newname, self.newdir, 'zip')
        else:
            flash('No file to customization')

    def prepare_file_for_user(self):
        if Path.is_file(Path(self.newdir, '[Content_Types].xml')):
            make_archive(Path(app.config['UPLOAD_FOLDER'], 'zipped'), 'zip', self.newdir)
            rename(Path(app.config['UPLOAD_FOLDER'], 'zipped.zip'), self.endfile)
        else:
            flash('No file to download')
    
    def clear_folder(self, folder):
        for filename in listdir(folder):
            file_path = Path(folder, filename)
            try:
                if path.isfile(file_path) or path.islink(file_path):
                    unlink(file_path)
                elif path.isdir(file_path):
                    rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))