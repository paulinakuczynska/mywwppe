from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Regexp
from flask_wtf.file import FileField, FileAllowed, FileRequired


class MyForm(FlaskForm):
    upload = FileField(
        label='file',
        validators=[
            FileRequired(),
            FileAllowed(['pptx'], '.pptx only')
        ]
    )
    hex1 = StringField(
        label='hex1',
        validators=[
            InputRequired(),
            Regexp('^[a-zA-Z0-9]{6,6}$', message='hex value must contain exactly six letters and/or digits'),
        ])
    name1 = StringField(
        label='name1',
        validators=[
            InputRequired(),
            Regexp('^[\w ]*$', message='you can use letters, digits, spaces and underscores')
        ])
    hex2 = StringField(
        label='hex2',
        name='hex',
        validators=[
            InputRequired(),
            Regexp('^[a-zA-Z0-9]{6,6}$', message='hex value must contain exactly six letters and/or digits'),
        ])
    name2 = StringField(
        label='name2',
        validators=[
            InputRequired(),
            Regexp('^[\w ]*$', message='you can use letters, digits, spaces and underscores')
        ])
    set_colors = SubmitField(
        label='set custom colors'
    )