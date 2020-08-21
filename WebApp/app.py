

import pandas as ps
import csv
import requests
from flask import Flask, request, render_template, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
import sqlite3
from datetime import date
from datetime import datetime , timedelta
import numpy as nm
from compareAnalysis.Analysis import AnalyzeData
from flask import flash
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import SubmitField , SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError
from wtforms.validators import DataRequired, Length
from datetime import date
import mysql.connector

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

app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = '18c228e2bb6d1a93c7dca14e0122ddd0ed46c221bbb086b988f06cdb219aa39d'
crsf = CSRFProtect(app)

def writeCSV(data,csvName,dataName):
    with open("url_for('static',filename='{}')".format(csvName), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "{}".format(dataName)])
        writer.writerow([1,data[0],data[1]])

def getDataFromDatabase(query):

    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'Predict'
    }

    myconn = mysql.connector.connect(**config)
    mycursor = myconn.cursor()

    mycursor.execute(query)
    result = mycursor.fetchall()

    return result



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/historical', methods=['GET', 'POST'])
def rainfall():
    myform = SelectDateForm()
    ateFrom = date
    dateTo = date
    hist = ''
    graphOrTable = ''
    error = "Sorry Invalid"

    if request.method == 'POST':
        dateFrom = request.form['date']
        dateTo = request.form['dateto']
        hist = request.form['historicalOptions']
        graphOrTable = request.form['displayOptions']
        myform.validatorisNone(myform.date,myform.dateto)
        myform.validateDateTo(myform.dateto)
        myform.validateINRange(myform.date,myform.dateto)

    if myform.date.data is not None and myform.dateto.data is not None and myform.validateDateTo(myform.dateto):
        flash("Date From from cannot be less than Date To")
        return redirect(url_for('rainfall', myform=myform))

    if myform.date.data is not None and myform.dateto.data is not None and myform.validateINRange(myform.date, myform.dateto):
        flash("Date is not in Range")
        return redirect(url_for('rainfall', myform=myform))

    if myform.date.data is not None and myform.dateto.data is not None and graphOrTable == 'table':

      return redirect(url_for('showData',dateTo=dateTo,dateFrom=dateFrom,hist=hist))


    if myform.date.data is not None and myform.dateto.data is not None and graphOrTable == 'graph':

        return redirect(url_for('showGraph', dateTo=dateTo, dateFrom=dateFrom, hist=hist))


    return render_template('historical.html', myform=myform)



@app.route('/showdata/<dateFrom>/<dateTo>/<hist>', methods=['GET', 'POST'])
def showData(dateFrom, dateTo, hist):

    # Read date from csv and use form input to send the view
    data = ps.read_csv('CorkAirport.csv', parse_dates=[0])
    Soil = data[['date', hist]]
    Soil['date'] = ps.to_datetime(Soil['date'])
    soilMask = (Soil['date'] >= dateFrom) & (Soil['date'] <= dateTo)
    myData = Soil.loc[soilMask]



    return render_template('showdata.html',myData=myData.values.tolist(), hist=hist, dateFrom=dateFrom, dateTo=dateTo)


@app.route('/ShowGraph/<dateFrom>/<dateTo>/<hist>', methods=['GET', 'POST'])
def showGraph(dateFrom, dateTo, hist):

    # Read date from csv and use form input to send the view
    data = ps.read_csv('CorkAirport.csv', parse_dates=[0])
    Soil = data[['date', hist]]
    Soil['date'] = ps.to_datetime(Soil['date'])
    soilMask = (Soil['date'] >= dateFrom) & (Soil['date'] <= dateTo)
    myData = Soil.loc[soilMask]


    writeCSV(myData.values.tolist(),'Graph.csv',hist)

    return render_template('ShowGraph.html')

@app.route('/weather')
def showWeather():
    todaysDate = date.today()
    dataBase = []
    todaysTime = datetime.today() + timedelta(hours=2,minutes=0)
    time = todaysTime.strftime('%H:%M %p')

    query = "SELECT * FROm predictions"
    getLen = getDataFromDatabase(query)

    for i in getLen:
        dataBase.append(i)
        length = len(dataBase)

    print("Length",length)

    newQuery = "SELECT * FROM predictions WHERE ID = {}".format(length)
    pred = getDataFromDatabase(newQuery)
    print("Query Successful")


    return render_template('weather.html', pred=pred,time=time)



@app.route('/TempComparison',methods=['GET'])
def TempCompare():
    object = AnalyzeData()
    myList = object.getDataAndAnalyze()
    predictionsList =[]
    graphYears = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']

    query = "SELECT * FROM predictions"

    result = getDataFromDatabase(query)

    for temp in result:
        predictionsList.append(temp[2])

    Max = nm.max(predictionsList)
    Min = nm.min(predictionsList)
    Average = nm.average(predictionsList)

    myList['2020Predictions'] = {'Max':Max,'Min':Min,'Average':round(Average)}

    preCSV = ps.DataFrame.from_dict(myList)
    preCSV.to_csv("url_for('static',Analysis.csv)", sep='\t', index=False)


    return render_template('Global.html',myList=myList,preCSV=preCSV)







if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    crsf.init_app(app)
