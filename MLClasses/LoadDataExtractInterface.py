import abc

class LoadDataExtractInterface(abc.ABC):
    "Load Data Interface"

    @abc.abstractmethod
    def loadDataAndFeatureExtraction(self,csvName):
        pass
        "used to lead and extract data"