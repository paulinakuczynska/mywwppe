# todo: 
# database, session, user-specific file storage
# error handler
# file size limit

from app import app
from flask import flash, redirect, render_template, request, send_file
from app.form import MyForm
from werkzeug.utils import secure_filename
from pathlib import Path
from app.models import manage_files, custom_colors, custom_margins

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def home():
    form = MyForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            if request.files:
                file = request.files['upload']
                if file.filename == '':
                    flash('No file name')
                    return redirect(request.url)
                if allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    myfile = manage_files.Files(filename, 'custom.zip')
                    myfile.clear_folder(app.config['UPLOAD_FOLDER'])
                    file.save(Path(app.config['UPLOAD_FOLDER'], filename))
                    myfile.prepare_file_for_editing()
                    values = []
                    names = []
                    for field in form.colors.data:
                        v = field['value']
                        n = field['name']
                        if v is not '':
                            values.append(v)
                            names.append(n)
                    if values:
                        col = custom_colors.CustomColors(names, values)
                        col.set_colors()
                    if form.remove_colors.data:
                        col = custom_colors.CustomColors(names, values)
                        col.remove_colors()
                    if form.margins.data:
                        marg = custom_margins.CustomMargins()
                        marg.set_zero_margins()
                    if values and form.remove_colors.data:
                        flash('You can\'t set and remove custom colors in the same time')
                        return redirect(request.url)
                    if values or form.remove_colors.data or form.margins.data:
                        myfile.prepare_file_for_user()
                        return render_template('downloads.html.jinja')
                    else:
                        flash('Nothing to customize')
                    return redirect(request.url)
                else:
                    flash('That file extension is not allowed')
                    return redirect(request.url)
    
    return render_template('home.html.jinja', title='Custom template', form=form)

@app.route('/download')
def return_file():
    return send_file(Path('uploads', 'new.pptx'), attachment_filename='new.pptx')