"""
Account object
"""

class Account(object):
    """
    Class representing an account on financial statemend
    """
    def __init__(self, data=None, parent=None, name=None):

        self._data = data
        self.parent = parent
        self._children = []
        if parent:
            self.parent.add_child(self)
        self.name = name

    def add_child(self, child):
        self._children.append(child)

    @property
    def data(self):
        """ If _data has been set, then consider it an override,
        else, return sum of children
        """
        if self._data is not None:
           return self._data
        else:
           return sum([child.data for child in self._children])

    @property
    def parent_name(self):
        if self.parent:
            return self.parent.name
        else:
            return None

    def __repr__(self):
        return "Account(name={name}, parent={parent})".format(
                name=self.name, parent=self.parent_name)
