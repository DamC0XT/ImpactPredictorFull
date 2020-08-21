import abc

class DataSplitInterface(abc.ABC):
    "Data Split Interface"

    @abc.abstractmethod
    def dataSplit(self,X,y):
        pass
        "Used for data splitting"

