from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, FormField, FieldList
from wtforms.validators import Regexp, Optional
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UploadForm(Form):
    upload = FileField(
        label='file',
        validators=[
            FileRequired(),
            FileAllowed(['pptx'], '.pptx only')
        ]
    )

class SubmitForm(Form):
    submit = SubmitField(
        label='submit'
    )

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

class CustomColors(FlaskForm):
    upload = FormField(UploadForm)
    colors = FieldList(FormField(ColorsForm), min_entries=10, max_entries=51)
    submit = FormField(SubmitForm)