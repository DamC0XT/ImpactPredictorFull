#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 15:25:45 2019

@author: roidanomaly
"""


import numpy as nm
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import jaccard_score

import matplotlib.pyplot as plt



def getData():
    data = pd.read_csv("rainfall.csv",parse_dates=[0])
    
    targets = data['rain']
    
    return data , targets

   
   
    
    

def KNearest():
    data, targets = getData()
    prediction = []
   
    regr = KNeighborsRegressor(n_neighbors=3)
    regr.fit(data[['ind','rain']],targets)
    
    
    

    print("Targets: ",targets)
    print("Prediction: ",regr.predict(data[['ind','rain']]))
    
    
    
    
def main():
    getData()
    KNearest()

main()
    

