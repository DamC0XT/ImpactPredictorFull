from flask_wtf import FlaskForm
from wtforms import SubmitField , StringField

from wtforms.validators import DataRequired, Length

class SelectDateForm(FlaskForm):
    date = StringField('Date from',validators=[DataRequired()],render_kw={"placeholder": "01-jan-2010"})
    dateto = StringField('Date to',validators=[DataRequired()],render_kw={"placeholder": "10-feb-2019"})
    
    submit = SubmitField('Submit')
