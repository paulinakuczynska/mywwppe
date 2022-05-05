# todo: error handler
# todo: file size limit

from app import app
from flask import flash, redirect, render_template, request
from app.form import CustomColors
from werkzeug.utils import secure_filename
from pathlib import Path
from app.models import manage_files, custom_colors


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
                    file.save(Path(app.config['UPLOAD_FOLDER'], filename))
                    flash(f'File {filename} uploaded')

                    values = []
                    names = []
                    for field in form.colors.data:
                        v = field['value']
                        n = field['name']
                        if v is not '':
                            values.append(v)
                            names.append(n)
                    flash(values)
                    flash(names)
                    if values:
                        manage_files.prepare_file_for_editing(filename, 'setcolors.zip')
                        custom_colors.set_custom_colors(names, values)
                        manage_files.prepare_file_for_user('nowy.pptx')
                    else:
                        flash('No color was given')
                    
                    return redirect(request.url)
                else:
                    flash('That file extension is not allowed')
                    return redirect(request.url)
    
    return render_template('colors.html.jinja', title='Set custom colors', form=form)

@app.route('/margins', methods=['GET', 'POST'])
def margins(): 
    return render_template('margins.html.jinja')