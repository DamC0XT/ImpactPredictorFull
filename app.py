import json

import pandas as ps
import requests
from flask import Flask, request, render_template, redirect, url_for, jsonify
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
from forms import SelectDateForm
import _sqlite3
import json
from datetime import date
from datetime import datetime
import numpy as nm
from compareAnalysis.Analysis import AnalyzeData

app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = '18c228e2bb6d1a93c7dca14e0122ddd0ed46c221bbb086b988f06cdb219aa39d'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/historical', methods=['GET', 'POST'])
def rainfall():
    form = SelectDateForm()
    dateFrom = date
    dateTo = date
    hist = ''
    graphOrTable = ''
    error = "Sorry Invalid"
    if request.method == 'POST':
        dateFrom = request.form['date']
        dateTo = request.form['dateto']
        hist = request.form['historicalOptions']
        graphOrTable = request.form['displayOptions']


    if form.date.data is None and form.dateto.data is None:
      return render_template('historical.html', form=form,error=error)


    if form.date.data is not None and form.dateto.data is not None and graphOrTable == 'table':
      return redirect(url_for('showData',dateTo=dateTo,dateFrom=dateFrom,hist=hist))





    return render_template('historical.html', form=form)












@app.route('/showdata/<dateFrom>/<dateTo>/<hist>', methods=['GET', 'POST'])
def showData(dateFrom, dateTo, hist):
    # Read date from csv and use form input to send the view
    data = ps.read_csv('CorkAirport.csv', parse_dates=[0])
    Soil = data[['date', hist]]
    Soil['date'] = ps.to_datetime(Soil['date'])
    soilMask = (Soil['date'] > dateFrom) & (Soil['date'] <= dateTo)
    myData = Soil.loc[soilMask]

    myData.to_csv("/home/roidanomaly/ImpactPredictor/static/Graph.csv", sep='\t', index=False)

    return render_template('showdata.html', myData=myData.values.tolist(), hist=hist, dateFrom=dateFrom, dateTo=dateTo)


@app.route('/weather')
def showWeather():
    engine = create_engine('sqlite:///predictions.db', echo=True)
    connection = engine.connect()
    metadata = MetaData()
    predictions = Table('predictions', metadata, autoload=True, autoload_with=engine)

    # query = select([predictions])
    todaysDate = date.today()
    newQuery = "SELECT * FROM predictions WHERE DATE LIKE '{}%'".format(todaysDate)
    ResultProxy = connection.execute(newQuery)

    pred = ResultProxy.fetchall()

    return render_template('weather.html', pred=pred)



@app.route('/TempComparison',methods=['GET'])
def TempCompare():
    object = AnalyzeData()
    myList = object.getDataAndAnalyze()
    predictionsList =[]

    engine = create_engine('sqlite:///predictions.db', echo=True)
    connection = engine.connect()
    metadata = MetaData()
    predictions = Table('predictions', metadata, autoload=True, autoload_with=engine)

    query = "SELECT * FROM predictions"
    ResultProxy = connection.execute(query)

    result = ResultProxy.fetchall()

    for temp in result:
        predictionsList.append(temp.Temperature)

    Max = nm.max(predictionsList)
    Min = nm.min(predictionsList)
    Average = nm.average(predictionsList)



    return render_template('Global.html',myList=myList,max=Max,min=Min,average=round(Average))







if __name__ == '__main__':
    app.run(debug=True)
