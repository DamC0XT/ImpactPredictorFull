import unittest
import pytest
from sqlalchemy import create_engine, MetaData, Table
class DatabaseTest(unittest.TestCase):

    def test_findAll(self):
        "Test if all database entries can be retrieved"

        engine = create_engine('sqlite:///predictions.db', echo=True)
        connection = engine.connect()
        metadata = MetaData()
        predictions = Table('predictions', metadata, autoload=True, autoload_with=engine)

        query = "SELECT * FROM predictions"
        ResultProxy = connection.execute(query)
        result = ResultProxy.fetchall()

        self.assertTrue(result)


    def test_findByDate(self):
        "Test if all a date in database entries can be retrieved"

        engine = create_engine('sqlite:///predictions.db', echo=True)
        connection = engine.connect()
        metadata = MetaData()
        predictions = Table('predictions', metadata, autoload=True, autoload_with=engine)

        query = "SELECT * FROM predictions where DATE ='2020-03-19 00:00:00.000000'"
        ResultProxy = connection.execute(query)
        result = ResultProxy.fetchall()

        self.assertTrue(result)

    def test_TempGreaterThanTen(self):
        "Test if all a Temp greater than ten in database entries can be retrieved"

        engine = create_engine('sqlite:///predictions.db', echo=True)
        connection = engine.connect()
        metadata = MetaData()
        predictions = Table('predictions', metadata, autoload=True, autoload_with=engine)

        query = "SELECT * FROM predictions where Temperature > 10"
        ResultProxy = connection.execute(query)
        result = ResultProxy.fetchall()

        self.assertTrue(result)


    def test_PressurelessThan1000(self):
        "Test if all a Temp greater than ten in database entries can be retrieved"

        engine = create_engine('sqlite:///predictions.db', echo=True)
        connection = engine.connect()
        metadata = MetaData()
        predictions = Table('predictions', metadata, autoload=True, autoload_with=engine)

        query = "SELECT * FROM predictions where Pressure < 1000"
        ResultProxy = connection.execute(query)
        result = ResultProxy.fetchall()

        self.assertTrue(result)
        




if __name__ == '__main__':
    unittest.main()