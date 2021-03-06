import pandas
from unittest import TestCase
from ..build import load_data
from inspect import getargspec


class TestLoadData(TestCase):
    def test_load_data_arguements(self):

        # Input parameters tests
        args = getargspec(load_data)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))

    def test_load_data_defaults(self):
    	args = getargspec(load_data)
    	self.assertEqual(args[3], None, "Expected default values do not match given default values")

    def test_load_data_dataframe(self):
        # Return type tests
        self.dataframe = load_data('data/house_prices_multivariate.csv')
        self.assertIsInstance(self.dataframe, pandas.DataFrame,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (type(self.dataframe)))

        # Return value tests
    def test_load_data_dataframe_iloc(self):
    	self.dataframe = load_data('data/house_prices_multivariate.csv')
    	self.assertEqual(self.dataframe.iloc[4,3], 5, "Return DataFrame does not match expected value")

    def test_load_data_dataframe_iloc1(self):
    	self.dataframe = load_data('data/house_prices_multivariate.csv')
    	self.assertEqual(self.dataframe.iloc[24, 34], 154000,"Return DataFrame value does not match expected value")
