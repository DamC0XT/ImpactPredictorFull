
import pandas as ps

class tenYearsData():

    def getDataFromCSV(self,dbname):

        data = ps.read_csv(dbname,parse_dates=[0])

        tenYears = data['date'] >= '2010-01-01'

        return data[tenYears]






    def tenYearsAPI(self,data):

        dateList = data['date'].tolist()
        tempList = data['Temp'].tolist()
        dates = []

        for i in dateList:
            dates.append(i.date())



        return dates , tempList





