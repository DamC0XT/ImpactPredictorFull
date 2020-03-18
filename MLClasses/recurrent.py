from __future__ import absolute_import, division, print_function, unicode_literals

import collections
import matplotlib.pyplot as plt
import numpy as np
import pandas as ps
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from flask import Flask, redirect, url_for, request, render_template, flash, redirect, url_for
from flask.json import jsonify
import simplejson as json
from bs4 import BeautifulSoup
import requests

from MLClasses.RecurrentInterface import RecurrentInterface


class RecurrentNet(RecurrentInterface):

    def __init__(self,csvName):
        predictions = []
        self.csvName = csvName
    
    
        


    def generator(self,batchSize,sequenceLength,numXInput,numYOutput,trainingNumber,xTrainScaled,yTrainScaled):

        while True:

            xShape = (batchSize,sequenceLength,numXInput)

            xBatch = np.zeros(shape=xShape,dtype=np.float16)

            yShape = (batchSize,sequenceLength,numYOutput)

            yBatch = np.zeros(shape=yShape,dtype=np.float16)

            for i in range(batchSize):

                index = np.random.randint(trainingNumber - sequenceLength)
                xBatch[i] = xTrainScaled[index:index+sequenceLength]
                yBatch[i] = yTrainScaled[index:index+sequenceLength]

                yield (xBatch,yBatch)




            
    
       



       



    def setUpNetwork(self,numXInput,numYOutput):
        model = tf.keras.Sequential()
        
        #Bidirection RNN processes sequence from start to end, but also backwards
       
        model.add((layers.GRU(units=512, return_sequences=True,input_shape=(None,numXInput))))

        
        # dense layer to give back outputs of one output
        model.add(layers.Dense(numYOutput,activation = 'sigmoid'))


        model.build((None,numXInput))
        model.summary()

        return model

    def RNNTraining(self,model,generator,validation):
        
       
        model.compile(loss='mse',optimizer='adam',metrics=['accuracy'])

        model.fit_generator(generator=generator,validation_data=validation,epochs=20,steps_per_epoch=100)

        

    def loadDataAndFeatureExtraction(self, csvName):
        # load dataset
        dataset = ps.read_csv(csvName, parse_dates=[0], index_col=0)
        # print to see if all has been read in
        print(dataset.head())
        # find correaltion in data that is best suited to temperature
        print(dataset.corr()['maxtp'])

        # setting timeshift
        dayShift = 1
        shiftSteps = dayShift * 24

        # from the correlation i decided i will use dewpt, vappr, wetb first

        dataset['DateTime'] = dataset.index.dayofyear

        features = dataset[['maxtp', 'cbl']]




        targets = dataset[['maxtp', 'cbl']]

        target = targets.shift(-shiftSteps)

        X = features.values[0:-shiftSteps]
        y = target.values[:-shiftSteps]

        return X, y

    def dataSplit(self, X, y):
        lengthData = len(X)
        split = 0.8

        trainingNumber = int(split * lengthData)

        x_train = X[:trainingNumber]
        x_test = y[trainingNumber:]

        y_train = X[0:trainingNumber]
        y_test = y[trainingNumber:]

        numXInput = X.shape[1]
        numYOutput = y.shape[1]

        return x_train, x_test, y_train, y_test, numXInput, numYOutput, trainingNumber

    def scale(self, x_train, x_test, y_train, y_test):
        xTrainScaler = MinMaxScaler()
        xTrainScaled = xTrainScaler.fit_transform(x_train)

        xTestScaled = xTrainScaler.fit_transform(x_test)

        yTrainScaler = MinMaxScaler()
        yTrainScaled = yTrainScaler.fit_transform(y_train)
        yTestScaled = yTrainScaler.fit_transform(y_test)

        return xTrainScaled, xTestScaled, yTrainScaled, yTestScaled, yTrainScaler
        
        
       
    def RNNPredict(self,model,X,yTrainScaler):
         
         preddy = yTrainScaler.fit_transform(X)
         pred = np.expand_dims(preddy,axis=0)
         print(pred)
         
         predictions = model.predict(pred)
         predictions = predictions.tolist()
         print(predictions)
         pred_P = yTrainScaler.inverse_transform(predictions[0])
         

         return pred_P.tolist()
         

        



if __name__ == '__main__':
    obj = RecurrentNet('temps_2019.csv')
    X,y = obj.loadDataAndFeatureExtraction(obj.csvName)
    x_train , x_test , y_train, y_test , numXInput , numYOutput , trainingNumber = obj.dataSplit(X,y)
    xTrainScaled ,xTestScaled , yTrainScaled, yTestScaled, yTrainScaler = obj.scale(x_train , x_test , y_train, y_test)
    batchSize = 300
    sequenceLength = 24 * 7  
    myGenerator = obj.generator(batchSize,sequenceLength,numXInput,numYOutput,trainingNumber,xTrainScaled,yTrainScaled)
    xBatch , yBatch = next(myGenerator)
    validationData = (np.expand_dims(xTestScaled,axis=0),np.expand_dims(yTestScaled,axis=0))
    mymodel =obj.setUpNetwork(numXInput,numYOutput)
    #obj.RNNTraining(mymodel,myGenerator,validationData)
    predictThis = np.array([[21.890,21.0],[15.723,21.0],[21.69,21.0]])
    #batchsize data 3 
    
    predict = obj.RNNPredict(mymodel,predictThis,yTrainScaler)
   
    
    print(type(predict))
    

   