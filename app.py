import json

import pandas as ps
import requests
from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String ,select
from forms import SelectDateForm
import _sqlite3
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
  hist = 0
  if request.method == 'POST':
    dateFrom = request.form['date']
    dateTo = request.form['dateto']
    hist = request.form['historicalOptions']
  if form.validate_on_submit():

    return redirect(url_for('showData',dateFrom=dateFrom,dateTo=dateTo,hist=hist))
 
  return render_template('historical.html',form=form)








@app.route('/showdata/<dateFrom>/<dateTo>/<hist>',methods=['GET','POST'])
def showData(dateFrom,dateTo,hist):

  data = ps.read_csv('CorkAirport.csv')
  Soil = data[['date', hist]]
  Soil['date'] = ps.to_datetime(Soil['date'])
  soilMask = (Soil['date'] > dateFrom) & (Soil['date'] <= dateTo)
  myData = Soil.loc[soilMask]


  return render_template('showdata.html',myData=myData.values.tolist(),hist=hist)


@app.route('/weather')
def showWeather():
  engine = create_engine('sqlite:///predictions.db',echo=True)
  connection = engine.connect()
  metadata = MetaData()
  predictions = Table('predictions', metadata, autoload=True, autoload_with=engine)

  query = select([predictions])

  ResultProxy = connection.execute(query)

  pred = ResultProxy.fetchall()
  print(pred)


  return render_template('weather.html',pred=pred)


  





if __name__ == '__main__':
  app.run(debug=True)
