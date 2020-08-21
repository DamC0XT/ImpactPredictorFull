import pandas as ps
import numpy as np

from MLClasses.LoadDataExtractInterface import LoadDataExtractInterface


class LoadDataExtract(LoadDataExtractInterface):

    def __init__(self, csvName):

        self.csvName = csvName

    def loadDataAndFeatureExtraction(self, csvName):
        # load dataset
        dataset = ps.read_csv(csvName, parse_dates=[0], index_col=0)
        # print to see if all has been read in
        print(dataset.head())
        # find correaltion in data that is best suited to temperature
        print(dataset.corr()['maxtp'])

        # setting timeshift
        dayShift = 1
        shiftSteps = dayShift * 7



        dataset['DateTime'] = dataset.index.dayofyear

        features = dataset[['maxtp', 'cbl']]

        targets = dataset[['maxtp', 'cbl']]

        target = targets.shift(-shiftSteps)

        X = features.values[0:-shiftSteps]
        y = target.values[:-shiftSteps]

        return X, y