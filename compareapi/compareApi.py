from flask import Flask, request, render_template, redirect, url_for, jsonify
from TenYearsData.tenyears import tenYearsData
app = Flask(__name__)
class compareApi():

    def __init__(self):
        self.dbname = "CorkAirport.csv"


@app.route('/',methods=['GET'])
def compApi():
    obj = tenYearsData()
    obj1 = compareApi()
    data = obj.getDataFromCSV(obj1.dbname)

    dates, temps = obj.tenYearsAPI(data)


    return jsonify({'Dates':dates,'Temps':temps})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
