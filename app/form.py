from decimal import Decimal, InvalidOperation
from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, FormField, FieldList, DecimalField
from wtforms.validators import Regexp, Optional, NumberRange
from flask_wtf.file import FileField, FileAllowed, FileRequired

class BetterDecimalField(DecimalField):
    def __init__(self, label=None, validators=None, places=2, rounding=None,
                 round_always=False, **kwargs):
        super(BetterDecimalField, self).__init__(
            label=label, validators=validators, places=places, rounding=
            rounding, **kwargs)
        self.round_always = round_always

    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = Decimal(valuelist[0])
                if self.round_always and hasattr(self.data, 'quantize'):
                    exp = Decimal('.1') ** self.places
                    if self.rounding is None:
                        quantized = self.data.quantize(exp)
                    else:
                        quantized = self.data.quantize(
                            exp, rounding=self.rounding)
                    self.data = quantized
            except (InvalidOperation, ValueError):
                self.data = None
                raise ValueError(self.gettext('Not a valid decimal value'))

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
    colors = FieldList(FormField(ColorsForm), min_entries=20, max_entries=51)
    submit = FormField(SubmitForm)

class CustomMargins(FlaskForm):
    upload = FormField(UploadForm)
    left = BetterDecimalField(
        label='left margin',
        round_always=2,
        default=0,
        validators=[
            NumberRange(min=0, max=10, message='the value should be between 0 and 10')
        ]
    )
    right = BetterDecimalField(
        label='right margin',
        round_always=2,
        default=0,
        validators=[
            NumberRange(min=0, max=10, message='the value should be between 0 and 10')
        ]
    )
    top = BetterDecimalField(
        label='top margin',
        round_always=2,
        default=0,
        validators=[
            NumberRange(min=0, max=10, message='the value should be between 0 and 10')
        ]
    )
    bottom = BetterDecimalField(
        label='bottom margin',
        round_always=2,
        default=0,
        validators=[
            NumberRange(min=0, max=10, message='the value should be between 0 and 10')
        ]
    )
    submit = FormField(SubmitForm)