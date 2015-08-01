"""
Tests for account
"""
import unittest

from pandas_accounting.core.account import Account
from pandas_accounting.core.tests.test_financials import periods,\
        create_rev_series, create_cost_series

from pandas import Series
from pandas.util.testing import assert_series_equal


class TestAccount(unittest.TestCase):
    def test_data(self):
        r = create_rev_series()
        c = create_cost_series()
        net_income = Account()
        revenue = Account(data=r, parent=net_income)
        cost = Account(data=c, parent=net_income)
        expected = Series([50,50,50,50,50], index=periods)
        assert_series_equal(net_income.data, expected)

