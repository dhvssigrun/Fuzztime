from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired

from fuzztime import Fuzztime

main = Blueprint('main', __name__,
                 template_folder='templates')


class FuzzEntryForm(FlaskForm):
    endpoint = StringField("Endpoint", validators=[DataRequired()])
    http_params = TextAreaField('HTTP params', validators=[DataRequired()], render_kw={"cols": 100, "rows": 15})
    payload_strings = TextAreaField('Payload strings', validators=[DataRequired()], render_kw={"cols": 100, "rows": 15})
    submit = SubmitField('Fuzz')


@main.route('/', methods=['GET', 'POST'])
def index():
    form = FuzzEntryForm()
    if form.validate_on_submit():
        fuzztime = Fuzztime(request.form['endpoint'],
                                request.form['http_params'],
                                request.form['payload_strings'])
        outputs = fuzztime.fuzz()
        return render_template('results.html', outputs=outputs)
    return render_template('index.html', form=form)
