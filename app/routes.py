# todo: error handler
# todo: file size limit

from app import app
from flask import flash, redirect, render_template, request
from app.form import MyForm
from werkzeug.utils import secure_filename
from pathlib import Path

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def set_colors_form():
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
                    file.save(Path(app.config['UPLOAD_FOLDER'], filename))
                    flash('File uploaded')
                    return redirect(request.url)
                else:
                    flash('That file extension is not allowed')
                    return redirect(request.url)
    
    return render_template(
        'mainpage.html.jinja', 
        title='Set custom colors', 
        form=form
        )