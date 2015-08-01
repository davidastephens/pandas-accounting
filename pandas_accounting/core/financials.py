"""
Financial statements
"""
from pandas_accounting.core.account import Account

class BaseStatement(object):
    def __init__(self, periods, data = None):
        self.periods = periods
        if data:
            self._data = data
        else:
            self._data = {}

    def __getitem__(self, key):
        return self._data[key].data

    def __getattr__(self,key):
        return self.__getitem__(key)

    def __setitem__(self, key, value):
        parent_name = self._parents[key]
        parent = self.get_or_create_account(parent_name)
        self._data[key] = Account(value, parent, name=key)

    def get_or_create_account(self, key):
        account = self._data.get(key, None)
        if account:
            return account
        else:
            if key == self._root:
                account = Account(name=key)
            else:
                parent_name = self._parents[key]
                parent = self.get_or_create_account(parent_name)
                account = Account(name=key, parent=parent)

            self._data[key] = account
            return account

    def actuals(self):
        pass

class Statements(BaseStatement):
    """
    Class representing the compilation of all 3 financial
    statements
    """
    pass


class BalanceSheet(BaseStatement):
    """
    Class representing the balance sheet
    """
    pass


class IncomeStatement(BaseStatement):
    """
    Class representing the income statement
    """
    _parents = {
            'EBITDA': 'Pre-Tax Income',
            'Pre-Tax Income': 'Net Income',
            'Revenue': 'EBITDA',
            'Cost of Goods Sold': 'EBITDA',
            'Cash Tax': 'Tax',
            'Deferred Tax': 'Tax',
            'Tax': 'Net Income',
            }

    _root = 'Net Income'

    # @property
    # def EBITDA(self):
    #     return self['Revenue'] + self['Cost of Goods Sold']


class CashFlowStatement(BaseStatement):
    """
    Class representing the cash flow statement
    """
    pass




