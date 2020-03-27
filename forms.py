from flask_wtf import FlaskForm
from wtforms import SubmitField , StringField, SelectField

from wtforms.validators import DataRequired, Length

class SelectDateForm(FlaskForm):
    historicalOptions = SelectField('Historical Options', choices=[('Temp', 'Temperature'), ('Rain', 'Rainfall'), ('Soil', 'Soil Temperature'), ('Grass', 'Min Grass Temperature'), ('Wind', 'WindSpeed')])
    date = StringField('Date from',validators=[DataRequired()],render_kw={"placeholder": "01-jan-2010"})
    dateto = StringField('Date to',validators=[DataRequired()],render_kw={"placeholder": "10-feb-2019"})
    
    submit = SubmitField('Submit')
