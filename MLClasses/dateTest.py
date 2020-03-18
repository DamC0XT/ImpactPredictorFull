import pandas as ps


class datesTest():



    def loadCSV(self,csvName):

        data = ps.read_csv(csvName)

        return data
    #checking dates in a range
    def dataSortSplit(self,data):
        data = ps.read_csv(csvName)
        Soil = data[['date','soil']]
        Soil['date'] = ps.to_datetime(Soil['date'])
        soilMask = (Soil['date'] > '01-jan-2010') & (Soil['date'] <= '02-feb-2010')
        print(Soil.loc[soilMask])





if __name__ == '__main__':
    obj = datesTest()
    csvName = 'CorkAirport.csv'
    data = obj.loadCSV(csvName)

obj.dataSortSplit(data)