from sklearn.preprocessing import MinMaxScaler

from MLClasses.TransformInterface import TransformInterface


class TransformScale(TransformInterface):

    def scale(self, x_train, x_test, y_train, y_test):
        xTrainScaler = MinMaxScaler()
        xTrainScaled = xTrainScaler.fit_transform(x_train)

        xTestScaled = xTrainScaler.fit_transform(x_test)

        yTrainScaler = MinMaxScaler()
        yTrainScaled = yTrainScaler.fit_transform(y_train)
        yTestScaled = yTrainScaler.fit_transform(y_test)

        return xTrainScaled, xTestScaled, yTrainScaled, yTestScaled, yTrainScaler