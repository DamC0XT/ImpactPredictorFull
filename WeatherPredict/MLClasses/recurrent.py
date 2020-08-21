from __future__ import absolute_import, division, print_function, unicode_literals

import collections

import numpy as np
import pandas as ps
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.python.keras.initializers import RandomUniform
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score


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
         

        




    

   