from flask import Flask, redirect, url_for, request, render_template, flash, redirect, url_for
import pandas as ps
import numpy as nm
from sqlalchemy import create_engine, Table,BIGINT ,TEXT, Column, Integer, String,Date,FLOAT, MetaData
from forms import SelectDateForm
from flask.json import jsonify
import requests
import tensorflow as tf
from recurrent import RecurrentNet
import pandas as ps
import numpy as np
import requests
import json
import os


app = Flask(__name__,static_url_path='/static')



app.config['SECRET_KEY'] = '18c228e2bb6d1a93c7dca14e0122ddd0ed46c221bbb086b988f06cdb219aa39d'


@app.route('/')
def index():

  return render_template('index.html')



@app.route('/historical',methods=['GET','POST'])
def rainfall():
  form = SelectDateForm()
  dateFrom = 0
  dateTo = 0

  if request.method == 'POST':
    dateFrom = request.form['date']
    dateTo = request.form['dateto']
  if form.validate_on_submit():

    return redirect(url_for('showData',dateFrom=dateFrom,dateTo=dateTo))
 
  return render_template('historical.html',form=form)


'''
@app.route('/rainfall/<year>',methods=['GET','POST'])
def rainfallAPI(year):
  
  engine = create_engine('sqlite:///ImpactWeather.db', echo=True)
  query = "SELECT * FROM rain where date like '%{}'".format(str(year))
  rain = engine.execute(query).fetchall()

  corkRain = []

  for data in rain:
     dataObj = {}
     dataObj['date'] = data.date
     dataObj['rainfall'] = data.rain
     corkRain.append(dataObj)

  return jsonify({'Cork Rainfall : = ' : corkRain})
'''






@app.route('/showdata/<dateFrom>/<dateTo>',methods=['GET','POST'])
def showData(dateFrom,dateTo):

  data = ps.read_csv('CorkAirport.csv')
  Soil = data[['date', 'soil']]
  Soil['date'] = ps.to_datetime(Soil['date'])
  soilMask = (Soil['date'] > dateFrom) & (Soil['date'] <= dateTo)
  myData = Soil.loc[soilMask]


  return render_template('showdata.html',myData=myData.values.tolist())


@app.route('/weather',methods=['GET'])
def showWeather():

  myRequest = requests.get('http://localhost:5050/predict')
  

 
  preds = myRequest.json()
  pred = json.dumps(preds)
  

  return render_template('weather.html',pred=pred)


  





if __name__ == '__main__':
  app.run(debug=True)
