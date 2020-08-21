from MLClasses.DataSplitInterface import DataSplitInterface


class DataSplit(DataSplitInterface):

    # Splitting data into 80 20
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