import unittest
import pytest
from MLClasses.DataSplit import DataSplit
from MLClasses.LoadDataExtract import LoadDataExtract
import numpy as nm


class MLClassTest(unittest.TestCase,DataSplit):

    def test_LoadDataExtractandDataSplit(self):
        csvName = '../dly3904.csv'
        object = LoadDataExtract(csvName)


        X,y = object.loadDataAndFeatureExtraction(object.csvName)
        result = X,y
        self.assertTrue(result)

        obj = DataSplit()
        x_train, x_test, y_train, y_test, numXInput, numYOutput, trainingNumber = obj.dataSplit(X,y)

        result1 = x_train,x_test
        result2 = y_train,y_test
        result3 = numXInput,numYOutput
        result4 = trainingNumber

        self.assertTrue(result1)

        self.assertTrue(result2)

        self.assertTrue(result3)

        self.assertTrue(result4)



if __name__ == '__main__':
    unittest.main()



