# todo: 
# database, session, user-specific file storage
# error handler
# file size limit

import os
from app import app
from flask import flash, redirect, render_template, request, send_file
from app.form import CustomColors, CustomMargins
from werkzeug.utils import secure_filename
from pathlib import Path
from app.models import manage_files, custom_colors, custom_margins

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def home(): 
    return render_template('home.html.jinja')

@app.route('/colors', methods=['GET', 'POST'])
def colors():
    form = CustomColors()
    if form.validate_on_submit():
        if request.method == 'POST':
            if request.files:
                file = request.files['upload-upload']
                if file.filename == '':
                    flash('No file name')
                    return redirect(request.url)
                if allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    myfile = manage_files.Files(filename, 'setcolors.zip')
                    myfile.clear_folder(app.config['UPLOAD_FOLDER'])
                    file.save(Path(app.config['UPLOAD_FOLDER'], filename))
                    values = []
                    names = []
                    for field in form.colors.data:
                        v = field['value']
                        n = field['name']
                        if v is not '':
                            values.append(v)
                            names.append(n)
                    # xml customization if at least one color was given
                    if values:
                        myfile.prepare_file_for_editing()
                        col = custom_colors.CustomColors(names, values)
                        col.set_colors()
                        myfile.prepare_file_for_user()
                        return render_template('downloads.html.jinja')
                    else:
                        flash('No color was given')
                    return redirect(request.url)
                else:
                    flash('That file extension is not allowed')
                    return redirect(request.url)
    
    return render_template('colors.html.jinja', title='Set custom colors', form=form)

@app.route('/margins', methods=['GET', 'POST'])
def margins():
    form = CustomMargins()
    if form.validate_on_submit():
        if request.method == 'POST':
            if request.files:
                file = request.files['upload-upload']
                if file.filename == '':
                    flash('No file name')
                    return redirect(request.url)
                if allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    myfile = manage_files.Files(filename, 'setmargins.zip')
                    myfile.clear_folder(app.config['UPLOAD_FOLDER'])
                    file.save(Path(app.config['UPLOAD_FOLDER'], filename))
                    left = form.left.data
                    right = form.right.data
                    top = form.top.data
                    bottom = form.bottom.data
                    myfile.prepare_file_for_editing()
                    marg = custom_margins.CustomMargins(left, right, top, bottom)
                    marg.set_margins()
                    myfile.prepare_file_for_user()
                    return render_template('downloads.html.jinja')
    return render_template('margins.html.jinja', form=form)

@app.route('/download')
def return_file():
    return send_file(Path('uploads', 'new.pptx'), attachment_filename='new.pptx')