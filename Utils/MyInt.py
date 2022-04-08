class MyInt(int):

    def __new__(cls, value, **kwargs):
        return super().__new__(cls, value)

    def __init__(self, value, **kwargs):
        self.__dict__.update(kwargs)

    def __iadd__(self, other):
        return self.__new__(type(self), self.__add__(other))

    def __isub__(self, other):
        return self.__new__(type(self), self.__sub__(other))

