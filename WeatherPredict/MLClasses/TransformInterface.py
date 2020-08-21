import abc


class TransformInterface(abc.ABC):
    "Scaling Interface"

    @abc.abstractmethod
    def scale(self, x_train, x_test, y_train, y_test):
        pass
    "Method to scale data for neural network to values between 0 and 1"