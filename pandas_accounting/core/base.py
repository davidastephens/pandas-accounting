"""
Base and utility classes for pandas-accounting.
"""

class Company(object):
    def __init__(self, shares=None):
        self.shares = shares


class Subsidiary(Company):
    def __init__(self):
        pass
