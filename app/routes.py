# todo: error handler
# todo: file size limit

from app import app
from flask import flash, redirect, render_template, request
from app.form import MyForm
from werkzeug.utils import secure_filename
from pathlib import Path
from app.models import manage_files, custom_colors


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def set_colors_form():
    form = MyForm()
    v = [form.hex1.data, form.hex2.data]
    values = list(v)
    n = [form.name1.data, form.name2.data]
    names = list(n)
    if form.validate_on_submit():
        if request.method == 'POST':
            if request.files:
                file = request.files['upload']
                if file.filename == '':
                    flash('No file name')
                    return redirect(request.url)
                if allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(Path(app.config['UPLOAD_FOLDER'], filename))
                    flash(f'File {filename} uploaded')
                    manage_files.prepare_file_for_editing(filename, 'setcolors.zip')
                    custom_colors.set_custom_colors(names, values)
                    manage_files.prepare_file_for_user('nowy.pptx')
                    return redirect(request.url)
                else:
                    flash('That file extension is not allowed')
                    return redirect(request.url)
    
    return render_template(
        'mainpage.html.jinja', 
        title='Set custom colors', 
        form=form
        )