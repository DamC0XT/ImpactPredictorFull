import requests
import numpy as nm

class AnalyzeData():

    def __init__(self):
        self.statsList = {}

    def getDataAndAnalyze(self):
        data = requests.get('http://172.18.0.1:8000')
        x = data.json()
        data2010year = "2010"
        data2011year = "2011"
        data2012year = "2012"
        data2013year = "2013"
        data2014year = "2014"
        data2015year = "2015"
        data2016year = "2016"
        data2017year = "2017"
        data2018year = "2018"
        data2019year = "2019"
        data2020year = "2020"

        data2010 = (x['Dates'][0:365], x['Temps'][0:365])
        data2010Max = nm.max(data2010[1])
        data2010Min = nm.min(data2010[1])
        data2010Average = nm.average(data2010[1])
        self.statsList[data2010year] = {'Max':data2010Max,'Min':data2010Min,'Average':round(data2010Average)}


        data2011 = (x['Dates'][366:731], x['Temps'][366:731])
        data2011Max = nm.max(data2011[1])
        data2011Min = nm.min(data2011[1])
        data2011Average = nm.average(data2011[1])
        self.statsList[data2011year] = {'Max':data2011Max, 'Min':data2011Min, 'Average':round(data2011Average)}

        data2012 = (x['Dates'][732:1097], x['Temps'][732:1097])
        data2012Max = nm.max(data2012[1])
        data2012Min = nm.min(data2012[1])
        data2012Average = nm.average(data2012[1])
        self.statsList[data2012year] = {'Max':data2012Max, 'Min':data2012Min, 'Average':round(data2012Average)}

        data2013 = (x['Dates'][1098:1463], x['Temps'][1098:1463])
        data2013Max = nm.max(data2013[1])
        data2013Min = nm.min(data2013[1])
        data2013Average = nm.average(data2013[1])
        self.statsList[data2013year] = {'Max':data2013Max, 'Min':data2013Min, 'Average':round(data2013Average)}

        data2014 = (x['Dates'][1464:1829], x['Temps'][1464:1829])
        data2014Max = nm.max(data2014[1])
        data2014Min = nm.min(data2014[1])
        data2014Average = nm.average(data2014[1])
        self.statsList[data2014year] = {'Max':data2014Max, 'Min':data2014Min, 'Average':round(data2014Average)}

        data2015 = (x['Dates'][1830:2195], x['Temps'][1830:2195])
        data2015Max = nm.max(data2015[1])
        data2015Min = nm.min(data2015[1])
        data2015Average = nm.average(data2015[1])
        self.statsList[data2015year] = {'Max':data2015Max, 'Min':data2015Min, 'Average':round(data2015Average)}

        data2016 = (x['Dates'][2196:2561], x['Temps'][2196:2561])
        data2016Max = nm.max(data2016[1])
        data2016Min = nm.min(data2016[1])
        data2016Average = nm.average(data2016[1])
        self.statsList[data2016year] = {'Max':data2016Max, 'Min':data2016Min, 'Average':round(data2016Average)}

        data2017 = (x['Dates'][2562:2927], x['Temps'][2562:2927])
        data2017Max = nm.max(data2017[1])
        data2017Min = nm.min(data2017[1])
        data2017Average = nm.average(data2017[1])
        self.statsList[data2017year] = {'Max':data2017Max, 'Min':data2017Min, 'Average':round(data2017Average)}

        data2018 = (x['Dates'][2928:3293], x['Temps'][2928:3293])
        data2018Max = nm.max(data2018[1])
        data2018Min = nm.min(data2018[1])
        data2018Average = nm.average(data2018[1])
        self.statsList[data2018year] = {'Max':data2018Max, 'Min':data2018Min, 'Average':round(data2018Average)}

        data2019 = (x['Dates'][3294:3659], x['Temps'][3294:3659])
        data2019Max = nm.max(data2019[1])
        data2019Min = nm.min(data2019[1])
        data2019Average = nm.average(data2019[1])
        self.statsList[data2019year] = {'Max':data2019Max, 'Min':data2019Min, 'Average':round(data2019Average)}

        data2020 = (x['Dates'][3660:3719], x['Temps'][3660:3719])
        data2020Max = nm.max(data2020[1])
        data2020Min = nm.min(data2020[1])
        data2020Average = nm.average(data2020[1])
        self.statsList[data2020year] = {'Max':data2020Max, 'Min':data2020Min, 'Average':round(data2020Average)}

        return self.statsList



