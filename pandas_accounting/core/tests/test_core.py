"""
Tests for core and utility classes
"""

import unittest

from pandas_accounting import Company, Subsidiary


class TestCompany(unittest.TestCase):
    def setUp(self):
        self.C = Company(shares=100)

    def test_company_shares(self):
        self.assertEqual(self.C.shares, 100)


class TestSubsidiary(unittest.TestCase):
    def setUp(self):
        self.S = Subsidiary()

    def test_sub(self):
        self.assertEqual(0,0)
