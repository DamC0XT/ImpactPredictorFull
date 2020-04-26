import app
import pytest
import unittest
from flask import Flask
from compareapi.compareApi import compApi
from compareapi.compareApi import compareApi
from test_client import TestClient

class FlaskTests(unittest.TestCase):



    def test_main_page(self):
        test = app.test_client(self)
        response = app.index
        self.assertTrue(response)

    def test_Historical(self):
        response = app.rainfall
        self.assertTrue(response)

    def test_GraphPage(self):
        response = app.showGraph
        self.assertTrue(response)

    def test_TablePage(self):
        response = app.showData
        self.assertTrue(response)

    def test_CompareApi(self):
        result = compApi
        self.assertTrue(result)













    if __name__ == "__main__":
        unittest.main()