from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, FormField, FieldList, BooleanField
from wtforms.validators import Regexp, Optional
from flask_wtf.file import FileField, FileAllowed, FileRequired

class ColorsForm(Form):
    value = StringField(
        label='value',
        validators=[
            Optional(),
            Regexp('^[a-zA-Z0-9]{6,6}$', message='hex value must contain exactly six letters and/or digits'),
        ]
    )
    name = StringField(
        label='name',
        validators=[
            Optional(),
            Regexp('^[\w ]*$', message='you can use letters, digits, spaces and underscores')
        ]
    )

class MyForm(FlaskForm):
    upload = FileField(
        label='file',
        validators=[
            FileRequired(),
            FileAllowed(['pptx'], '.pptx only')
        ]
    )
    colors = FieldList(FormField(ColorsForm), min_entries=20, max_entries=51)
    remove_colors = BooleanField(label='remove custom colors')
    margins = BooleanField(label='set margins')
    submit = SubmitField(label='submit')