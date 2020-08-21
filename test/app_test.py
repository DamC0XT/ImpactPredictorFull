import os
import tempfile

import pytest
from flask import Flask,request
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

from WebApp.app import app

class SelectDateForm(FlaskForm):
    displayOptions = SelectField('Display Options', choices=[('table','Table'),('graph','Graph')])
    historicalOptions = SelectField('Historical Options', choices=[('Temp', 'Temperature'), ('Rain', 'Rainfall'), ('Soil', 'Soil Temperature'), ('Grass', 'Min Grass Temperature'), ('Wind', 'WindSpeed')])
    date = DateField('Date from',validators=[DataRequired()])
    dateto = DateField('Date to',validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validateDateTo(form,field):
        if field.data < form.date.data:
            return True


    def validateINRange(form,field1,field2):
        if field1.data < date(1980, 1, 1) or field1.data  > date (2019,12,31) and field2.data < date(1980,1,1) or field2.data > date(2019,12,31):
           return True

    def validatorisNone(form,field1,field2):
        if field1.data is None and field2.data is None:
            return True

from datetime import date


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_Index(client):

    response = client.get('/')
    assert 'b"200"',response.data.status_code



def test_Historical(client):

    response = client.get('/historical')
    assert 'b"200"',response.data.status_code

def test_Weather(client):

    response = client.get('/weather')
    assert 'b"200"',response.data.status_code

def test_Global(client):

    response = client.get('/TempComparison')
    assert 'b"200"',response.data.status_code

def test_showGraph(client):

    response = client.get('/showGraph')
    assert 'b"200"',response.data.status_code

def test_showTable(client):

    response = client.get('/showData')
    assert 'b"200"',response.data.status_code

def useForm(client,dateFrom,dateTo,hist,type):

    return client.post('/historical',data=dict(
        dateFrom=dateFrom,
        dateTo=dateTo,
        hist=hist,
        type=type
    ),follow_redirects=True)

def test_Form(client):

    response = useForm(client, dateFrom= "2010-01-12",dateTo="2011-01-12",hist="Temp",type="table")
    assert 'b"Form Worked"', response.data


def test_FormGraph(client):

    response = useForm(client, dateFrom= "2010-01-12",dateTo="2011-01-12",hist="Soil",type="graph")
    assert 'b"Form Worked"', response.data
