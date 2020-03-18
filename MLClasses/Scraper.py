

import requests
import time
import xml.etree.ElementTree as ET

from MLClasses.ScraperInterface import ScraperInterface


class WeatherAPI(ScraperInterface):


    def __init__(self):
        self.weatherDict = {}
        self.temp = []
        self.pressure = []
        self.timeTo = []
        self.timeFrom = []
    def ApiCall(self):
         # api call to get todays data for cork.. Try filter datafrom this
         y = requests.get('http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=51.8960528;long=-8.498069')


         #reading the xml api request into an ElementTree
         root = ET.fromstring(y.content)

         #Loops throught th Element tree and append wanted items into lists
         for child in root.iter('time'):

             self.timeFrom.append(child.attrib['from'])
             self.timeTo.append(child.attrib['to'])

         for child in root.iter('temperature'):

             self.temp.append(child.attrib['value'])


         for child in root.iter('pressure'):

            self.pressure.append(child.attrib['value'])

         #making a dictionary from the lists to return
         self.weatherDict['Temp'] = self.temp
         self.weatherDict['Pressure'] = self.pressure
         self.weatherDict['TimeFrom'] = self.timeFrom
         self.weatherDict['TimeTo'] = self.timeFrom

         return self.weatherDict



















