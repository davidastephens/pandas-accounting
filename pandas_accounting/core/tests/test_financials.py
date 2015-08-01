"""
Tests for financial statements
"""

import unittest

from pandas_accounting import Statements, IncomeStatement
from pandas_accounting.core.account import Account

from pandas import Series
from pandas import date_range
from pandas.util.testing import assert_series_equal

periods = date_range("2010", "2015", freq="A")

def create_rev_series():
        return Series([100,100,100,100,100], index=periods)

def create_cost_series():
        return Series([-50,-50,-50,-50,-50], index=periods)

def create_income_statement():
        s = IncomeStatement(periods)
        r = create_rev_series()
        c = create_cost_series()
        dt = Series([-20,-20,-20,-20,-20], index=periods)
        s['Revenue'] = r
        s['Cost of Goods Sold'] = c
        s['Deferred Tax'] = dt
        return s

class TestIncomeStatement(unittest.TestCase):

    def setUp(self):
        self.s = create_income_statement()

    def test_ebitda(self):
        expected = Series([50,50,50,50,50], index=self.s.periods)
        ebitda = self.s.EBITDA
        assert_series_equal(ebitda, expected)

    def test_net_income(self):
        expected = Series([30,30,30,30,30], index=self.s.periods)
        net_income= self.s['Net Income']
        assert_series_equal(net_income, expected)

    #Features to be added
    # def test_actuals(self):
    #     self.s.actuals

