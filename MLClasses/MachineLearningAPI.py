from flask import Flask, redirect, url_for, request, render_template, flash, redirect, url_for
from flask.json import jsonify

app = Flask(__name__)
class MachineAPI():

    @app.route('/predict', methods=['GET', 'POST'])
    def predictapi():
        global mymodel
        mymodel = obj.setUpNetwork(numXInput, numYOutput)
        # obj.RNNTraining(mymodel,myGenerator,validationData)

        predictThis = np.array([[3, 0.0], [2, 0.0], [7, 0.0], [11, 0.0], [8, 0.0]])
        predict = obj.RNNPredict(mymodel, predictThis, yTrainScaler)

        newList = []
        for i in predict:
            data = {}
            data = {"TodaysTemp": i}
            newList.append(data)

        return jsonify({'Cork Temp: = ': newList})




if __name__ == '__name__':
    app.run(port=5050,debug=True)
