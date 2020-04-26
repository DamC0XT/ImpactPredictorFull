import unittest
import pytest
from MLClasses.Scraper import WeatherAPI

class ApiTest(unittest.TestCase):

    def test_DataRetrieved(self):

        obj = WeatherAPI()
        obj.ApiCall()

        result = obj.ApiCall()

        self.assertTrue(result)
        

if __name__ == '__main__':
    unittest.main()