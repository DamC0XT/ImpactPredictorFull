import abc

class ScraperInterface(abc.ABC):
    "Interface for reading met eireann weather api"

    @abc.abstractmethod
    def ApiCall(self):
        pass;
    "function to read api and put into dictionary to pass"