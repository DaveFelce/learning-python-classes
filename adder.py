class Adder():

    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return self.add(other)

    def add(self, y):
        raise NotImplementedError


class ListAdder(Adder):

    def add(self, y):
        return self.data + y


class DictAdder(Adder):

    def add(self, dict_y):
        return dict(self.data, **dict_y)
