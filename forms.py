from flask_wtf import FlaskForm
from wtforms import SubmitField , SelectField
from wtforms.fields.html5 import DateField

from wtforms.validators import DataRequired, Length

class SelectDateForm(FlaskForm):
    historicalOptions = SelectField('Historical Options', choices=[('Temp', 'Temperature'), ('Rain', 'Rainfall'), ('Soil', 'Soil Temperature'), ('Grass', 'Min Grass Temperature'), ('Wind', 'WindSpeed')])
    date = DateField('Date from', format('%d-%b-%Y'))
    dateto = DateField('Date to',format('%d-%b-%Y'))
    submit = SubmitField('Submit')

