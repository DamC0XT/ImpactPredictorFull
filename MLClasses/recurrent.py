from __future__ import absolute_import, division, print_function, unicode_literals

import collections
import matplotlib.pyplot as plt
import numpy as np
import pandas as ps
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.python.keras.initializers import RandomUniform
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



        model.add(layers.Dense(numYOutput,activation='linear'))

        model.build((None, numXInput))
        model.summary()

        return model

    def RNNTraining(self,model,generator,validation):
        
       
        model.compile(loss='mse',optimizer='adam',metrics=['accuracy'])

        model.fit_generator(generator=generator,validation_data=validation,epochs=50,steps_per_epoch=100)

        




        
       
    def RNNPredict(self,model,X,yTrainScaler):
         
         preddy = yTrainScaler.fit_transform(X)
         pred = np.expand_dims(preddy,axis=0)

         
         predictions = model.predict(pred)
         predictions = predictions.tolist()

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
    

   