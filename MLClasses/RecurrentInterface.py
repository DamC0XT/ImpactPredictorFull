import abc

class RecurrentInterface(abc.ABC):
    "Interface for reccurent network"

    @abc.abstractmethod
    def generator(self, batchSize, sequenceLength):
        pass
    "Function for making batch to train network"

    @abc.abstractmethod
    def setUpNetwork(self, numXInput, numYOutput):
        pass
    "Function to set up nueral network "

    @abc.abstractmethod
    def RNNTraining(self,model,generator,validation):
        pass

    "Function to train up neural network "

    @abc.abstractmethod
    def RNNPredict(self,model,X,yTrainScaler):
        pass

    "function to Predict data "