from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as ps
from sqlalchemy import create_engine ,MetaData,Table,Column,Float,Integer,DateTime
import sqlite3
import datetime
from MLClasses.DataSplit import DataSplit
from MLClasses.LoadDataExtract import LoadDataExtract
from MLClasses.Transform import TransformScale
from MLClasses.recurrent import RecurrentNet
from MLClasses.Scraper import WeatherAPI
import mysql.connector


class Run(LoadDataExtract,DataSplit,TransformScale,RecurrentNet,WeatherAPI):

    def __init__(self):
        self.predictions = []


    def dbinsert(pred):
        date = datetime.date.today()
        ID = 50
        query = "INSERT INTO predictions (Date ,Temperature,Pressure) VALUES ('{}','{}','{}')".format(date,pred[0][0],pred[0][1])


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
        myconn.commit()
        print("Prediction Inserted Successfully")


    if __name__ == '__main__':

        obj = LoadDataExtract('dly3904.csv')
        objSplit = DataSplit()
        objScale = TransformScale()
        objNetwork = RecurrentNet('dly3904.csv')
        objScrape = WeatherAPI()
        csvName = obj.csvName
        X,y  = obj.loadDataAndFeatureExtraction(csvName)
        x_train, x_test, y_train, y_test, numXInput, numYOutput, trainingNumber = objSplit.dataSplit(X, y)
        xTrainScaled, xTestScaled, yTrainScaled, yTestScaled, yTrainScaler = objScale.scale(x_train, x_test, y_train, y_test)
        batchSize = 1000
        sequenceLength = 1 * 7
        myGenerator = objNetwork.generator(batchSize, sequenceLength,numXInput,numYOutput,trainingNumber,xTrainScaled,yTrainScaled)
        xBatch, yBatch = next(myGenerator)
        validationData = (np.expand_dims(xTestScaled, axis=0), np.expand_dims(yTestScaled, axis=0))
        mymodel = objNetwork.setUpNetwork(numXInput, numYOutput)
        #objNetwork.RNNTraining(mymodel, myGenerator, validationData)

        #prediction = []
        predictThis = objScrape.ApiCall()

        predict = ps.DataFrame(predictThis,columns=['Temp','Pressure'])
        check = predict.iloc[0:1].values

        #predictThis1 = np.array([[21.890, 1000.0], [15.723, 1000.0], [21.69, 1000.9]])

        pred = objNetwork.RNNPredict(mymodel,check,yTrainScaler)
        dbinsert(pred)
















